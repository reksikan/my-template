import subprocess

from aiologger.loggers.json import JsonLogger
from sqlalchemy import text
from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    async_sessionmaker, create_async_engine)
from sqlalchemy.ext.asyncio.session import _AsyncSessionContextManager

logger = JsonLogger.with_default_handlers()


class DbManager:

    def __init__(self, async_engine: AsyncEngine):
        self._async_engine = async_engine
        self._async_session = async_sessionmaker(
            self._async_engine,
            expire_on_commit=False,
        )

    async def healthcheck(self) -> bool:
        try:
            async with self.session() as session:
                await session.execute(text('CREATE TEMPORARY TABLE test (testclmn TEXT) ON COMMIT DROP;'))
                return True
        except Exception:
            logger.exception('Database healthcheck failed')
            return False

    def session(self) -> _AsyncSessionContextManager[AsyncSession]:
        return self._async_session.begin()


def create_db_manager(
    connection_url: str,
    need_migrations: bool = True
) -> DbManager:
    engine = create_async_engine(connection_url)

    if need_migrations:
        subprocess.run(
            'alembic upgrade head',
            check=True,
            shell=True
        )

    return DbManager(engine)

