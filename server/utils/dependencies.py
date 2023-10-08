from fastapi import Depends
from fastapi_users.authentication import JWTStrategy
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from server.config.factory import settings
from server.database.users import UserManager
from server.models import get_async_database_session
from server.models.users import OAuthAccount, User


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.JWT_SECRET, lifetime_seconds=3600)


async def get_user_db(session: AsyncSession = Depends(get_async_database_session)):
    yield SQLAlchemyUserDatabase(session, User, OAuthAccount)


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
