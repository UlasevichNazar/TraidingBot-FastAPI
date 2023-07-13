import os
import time
from typing import List
from celery.utils.log import get_task_logger
import httpx
from app.celery_app import celery_app
from async_to_sync import coroutine
from app.parsing.repositories.parser import AssetRepository
from app.parsing.services import AssetService

logger = get_task_logger(__name__)


@celery_app.task()
def parsing(assets_collection: List[str]):
    api_key = os.environ.get("API_KEY")
    for asset in assets_collection:
        url = f"{os.environ.get('URL')}symbol={asset}&apikey={api_key}"
        response = httpx.get(url)

        if response.status_code == 200:
            file = response.json()
            logger.info(file)
            upsert.delay(file["Global Quote"])

        time.sleep(5)


@celery_app.task()
def upsert(file: dict):
    coroutine(AssetService(AssetRepository()).update_price(file))
