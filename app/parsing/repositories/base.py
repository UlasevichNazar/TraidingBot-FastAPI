class AssetNotFound(Exception):
    pass


class BaseRepository:
    def __init__(self, collection) -> None:
        self.collection = collection

    async def get(self, filter: dict):
        async for asset in self.collection.find(filter):
            yield asset

    async def create(self, file: dict):
        await self.collection.insert_one(file)

    async def update(self, filter: dict, file: dict, upsert: bool = False):
        res = await self.collection.update_one(filter, {"$set": file}, upsert=upsert)
        if not res.matched_count and not upsert:
            raise AssetNotFound(f"Сan't find asset to update {filter}")

    async def delete(self, filter: dict):
        result = await self.collection.delete_one(filter)
        return result
