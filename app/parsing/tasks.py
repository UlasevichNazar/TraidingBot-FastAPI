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
        response = await client.get(url)
    return response


@celery_app.task()
def parsing(assets_collection: List[str]):
    api_key = setting.API_KEY
    for asset in assets_collection:
        url = f"{setting.URL}symbol={asset}&apikey={api_key}"
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(get_response(url))

        if response.status_code == 200:
            file = response.json()
            logger.info(file)
            upsert.delay(file["Global Quote"])

    time.sleep(5)
    # values = ([{'01. symbol': 'AAPL', '05. price': 193.73}, {'01. symbol': 'LTC', '05. price': 34.35},
    #            {'01. symbol': 'EOS', '05. price': 18.62}, {'01. symbol': 'LUNA', '05. price': 8.84},
    #            {'01. symbol': 'PPC', '05. price': 24.49},
    #            {'01. symbol': 'BTC', '05. price': 12.00}])
    # for file in values:
    #     upsert.delay(file) # for testing (used when request limit is exceeded)


@celery_app.task()
def upsert(file: dict):
    coroutine(AssetService(AssetRepository()).update_price(file))
