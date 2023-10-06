from fastapi_users.db import SQLAlchemyBaseOAuthAccountTable, SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, relationship

from server.models import Base


class OAuthAccount(SQLAlchemyBaseOAuthAccountTable, Base):
    pass


class User(SQLAlchemyBaseUserTable, Base):
    oauth_accounts: Mapped[list[OAuthAccount]] = relationship(OAuthAccount, lazy="joined")
