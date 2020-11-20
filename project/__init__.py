
from fastapi import FastAPI

from project.config import DB_MAPPER
from api.link import router

DB_MAPPER()
app = FastAPI()

app.include_router(router)
