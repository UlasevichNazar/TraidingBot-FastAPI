from fastapi import FastAPI

from app.parsing.controllers import asset_router

app = FastAPI()
app.include_router(asset_router)
