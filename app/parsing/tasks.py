import time
from typing import List

import httpx
from async_to_sync import coroutine
from celery.utils.log import get_task_logger

from app.celery_app import celery_app
from app.parsing.repositories.parser import AssetRepository
from app.parsing.services import AssetService

logger = get_task_logger(__name__)
from config.config import setting


@celery_app.task()
def parsing(assets_collection: List[str]):
    api_key = setting.API_KEY
    for asset in assets_collection:
        url = f"{setting.URL}symbol={asset}&apikey={api_key}"
        response = httpx.get(url)

        if response.status_code == 200:
            file = response.json()
            logger.info(file)
            upsert.delay(file["Global Quote"])

        time.sleep(5)


@celery_app.task()
def upsert(file: dict):
    coroutine(AssetService(AssetRepository()).update_price(file))
