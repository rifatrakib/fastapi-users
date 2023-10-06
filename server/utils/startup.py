from sqlalchemy.ext.asyncio import create_async_engine

from server.config.factory import settings
from server.models.users import User


async def create_database_tables():
    engine = create_async_engine(settings.RDS_URI)
    async with engine.begin() as connection:
        await connection.run_sync(User.metadata.create_all)
