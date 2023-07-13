class BaseRepository:
    def __init__(self, collection) -> None:
        self.collection = collection

    async def get(self, filter: dict):
        async for asset in self.collection.find(filter):
            yield asset

    async def create(self, file: dict):
        await self.collection.insert_one(file)

    async def update(self, filter: dict, file: dict, upsert: bool = False):
        await self.collection.update_one(filter, {"$set": file}, upsert=upsert)

    async def delete(self, filter: dict):
        await self.collection.delete_one(filter)
