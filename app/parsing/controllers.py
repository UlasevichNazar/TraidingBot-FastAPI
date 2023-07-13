from fastapi import APIRouter
from app.parsing.repositories.parser import AssetRepository
from app.parsing.services import AssetService
from async_to_sync import coroutine

asset_router = APIRouter(prefix='/assets')


@asset_router.get('/')
async def get_asset():
    assets = await AssetService(AssetRepository()).get_assets()
    return assets


@asset_router.get('/update/')
async def upd():
    return await AssetService(AssetRepository()).update_price({
        '01. symbol': 'aaaa',
        '05. price': 1212.33
    })
