import json

from bson import json_util
from fastapi import FastAPI

from app.parsing.controllers import asset_router
from app.parsing.tasks import parsing
from app.database_app import collection

app = FastAPI()
app.include_router(asset_router)

