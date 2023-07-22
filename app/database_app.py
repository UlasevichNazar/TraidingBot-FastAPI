import os

import motor.motor_asyncio

_mongo_url = f"mongodb://{os.environ.get('MONGO_HOST')}:{os.environ.get('MONGO_PORT')}"

client = motor.motor_asyncio.AsyncIOMotorClient(_mongo_url)
database = client.db

collection = database.assets
