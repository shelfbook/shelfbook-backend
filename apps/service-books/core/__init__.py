from fastapi import FastAPI
from api import router


class AppCreator:
    def __init__(self):
        self.app = FastAPI(
            title="Сервис книг",
            version="1.0.0"
        )
        self._init_routers()

    def _init_routers(self):
        self.app.include_router(router)

    def get(self) -> FastAPI:
        return self.app


app = AppCreator().get()
