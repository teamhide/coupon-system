from sqlalchemy import Column, Unicode, BigInteger, Integer

from core.db import Base
from core.db.mixins import TimestampMixin


class Coupon(Base, TimestampMixin):
    __tablename__ = "coupon"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(Unicode(255), nullable=False)
    price = Column(Unicode(255), nullable=False)
    quantity = Column(Integer, nullable=False)
