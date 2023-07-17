from fastapi import APIRouter

from app.parsing.repositories.parser import AssetRepository
from app.parsing.services import AssetService

asset_router = APIRouter(prefix="/assets")


@asset_router.get("/")
async def get_asset():
    assets = await AssetService(AssetRepository()).get_assets()
    return assets
