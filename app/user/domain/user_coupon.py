from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from core.db import Base
from core.db.mixins import TimestampMixin


class UserCoupon(Base, TimestampMixin):
    __tablename__ = "user_coupon"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("user.id"))
    coupon_id = Column(BigInteger, ForeignKey("coupon.id"))

    user = relationship("User", lazy="select")
    coupon = relationship("Coupon", lazy="select")
