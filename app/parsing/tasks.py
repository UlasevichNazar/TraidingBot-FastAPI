import asyncio
import time
from typing import List

import httpx
from async_to_sync import coroutine
from celery.utils.log import get_task_logger

from app.celery_app import celery_app
from app.parsing.repositories.parser import AssetRepository
from app.parsing.services import AssetService
from config.config import setting

logger = get_task_logger(__name__)


async def get_response(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=20)
    return response


@celery_app.task()
def parsing(assets_collection: List[str]):
    api_key = setting.API_KEY
    for asset in assets_collection:
        url = f"{setting.URL}&symbol={asset}&apikey={api_key}"
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(get_response(url))

        if response.status_code == 200:
            file = response.json()
            logger.info(file)
            upsert.delay(file[f"{setting.global_quote}"])

    time.sleep(20)
    # values = [
    #     {f"{setting.symbol}": "AAPL", f"{setting.price}": 193.73},
    #     {f"{setting.symbol}": "LTC", f"{setting.price}": 34.35},
    #     {f"{setting.symbol}": "EOS", f"{setting.price}": 18.62},
    #     {f"{setting.symbol}": "LUNA", f"{setting.price}": 8.84},
    #     {f"{setting.symbol}": "PPC", f"{setting.price}": 24.49},
    #     {f"{setting.symbol}": "BTC", f"{setting.price}": 12.00},
    # ]
    # for file in values:
    #     upsert.delay(file)  # for testing (used when request limit is exceeded)


@celery_app.task()
def upsert(file: dict):
    coroutine(AssetService(AssetRepository()).update_price(file))
