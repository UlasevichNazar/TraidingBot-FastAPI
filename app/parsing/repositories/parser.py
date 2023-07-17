from app.database_app import collection
from app.parsing.repositories.base import BaseRepository
from app.parsing.schemas import Schema
from app.producer import send_update_asset_info


class AssetRepository(BaseRepository):
    def __init__(self, collection=collection):
        super().__init__(collection)

    async def get_assets(self):
        async for asset in self.get({}):
            print(asset)
        return [Schema(**asset).model_dump() async for asset in self.get({})]

    async def update_asset_price(self, file: dict, filter):
        await self.update(filter, file, upsert=True)
        await (send_update_asset_info(file))
