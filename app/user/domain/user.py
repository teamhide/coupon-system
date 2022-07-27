from sqlalchemy import Column, Unicode, BigInteger

from core.db import Base
from core.db.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(Unicode(255), nullable=False)
    password = Column(Unicode(255), nullable=False)

    @classmethod
    def create(cls, name: str, password: str) -> "User":
        return cls(name=name, password=password)
