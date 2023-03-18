import uvicorn
from fastapi import FastAPI

from config import POSTGRES_URL, SERVER_HOST, SERVER_PORT
from src.api.http import HTTPServer
from src.clients.manager import ClientManager
from src.db.manager import create_db_manager


def get_app() -> FastAPI:
    db_manager = create_db_manager(POSTGRES_URL)
    client_manager = ClientManager()

    http_server = HTTPServer(client_manager, db_manager)
    return http_server.app


if __name__ == '__main__':
    uvicorn.run(get_app(), host=SERVER_HOST, port=SERVER_PORT)
