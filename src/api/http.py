from fastapi import FastAPI, Request, Response

from src.clients.manager import ClientManager
from src.db.manager import DbManager


class HTTPServer:

    def __init__(self, client_manager: ClientManager, db_manager: DbManager):
        self._client_manager = client_manager
        self._db_manager = db_manager

        app = FastAPI()

        app.add_api_route('/', self.ping)

        self._app = app

    @property
    def app(self):
        return self._app

    async def ping(self, _: Request):
        await self._db_manager.healthcheck()
        return Response(status_code=200)