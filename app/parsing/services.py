from app.parsing.repositories.parser import AssetRepository
from config.config import setting


class AssetService:
    def __init__(self, repository: AssetRepository):
        self.repository = repository

    async def get_assets(self):
        return await self.repository.get_assets()

    async def update_price(self, file: dict):
        filter = {"name": file[f"{setting.symbol}"]}
        file = {
            "name": file[f"{setting.symbol}"],
            "current_price": file[f"{setting.price}"],
        }
        return await self.repository.update_asset_price(file, filter)
