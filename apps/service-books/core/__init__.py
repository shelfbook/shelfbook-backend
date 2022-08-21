from fastapi import FastAPI
from handlers import router
from core.db import metadata, engine
from domain import authors, books


class AppCreator:

    def __init__(self):
        self._init_db()
        self.app = FastAPI(
            title="Сервис книг",
            version="1.0.0"
        )
        self._init_routers()

    def _init_db(self):
        pass

    def _init_routers(self):
        self.app.include_router(router)

    def get(self) -> FastAPI:
        return self.app


metadata.create_all(bind=engine)
app = AppCreator().get()

