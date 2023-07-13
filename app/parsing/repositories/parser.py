from app.parsing.repositories.base import BaseRepository

from app.parsing.schemas import Schema
from app.database_app import collection


class AssetRepository(BaseRepository):
    def __init__(self, collection=collection):
        super().__init__(collection)

    async def get_assets(self):
        return [Schema(**asset).model_dump() async for asset in self.get({})]

    async def update_asset_price(self, file: dict, filter):
        await self.update(filter, file, upsert=True)
