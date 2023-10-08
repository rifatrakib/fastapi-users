from fastapi_users.db import SQLAlchemyBaseOAuthAccountTable, SQLAlchemyBaseUserTable
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.models import Base


class OAuthAccount(SQLAlchemyBaseOAuthAccountTable, Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="cascade"), nullable=False)


class User(SQLAlchemyBaseUserTable, Base):
    oauth_accounts: Mapped[list[OAuthAccount]] = relationship(OAuthAccount)
