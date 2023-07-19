from app.parsing.repositories.parser import AssetRepository


class AssetService:
    def __init__(self, repository: AssetRepository):
        self.repository = repository

    async def get_assets(self):
        return await self.repository.get_assets()

    async def update_price(self, file: dict):
        filter = {"name": file["01. symbol"]}
        file = {"name": file["01. symbol"], "current_price": file["05. price"]}
        return await self.repository.update_asset_price(file, filter)
