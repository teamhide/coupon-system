import logging
from typing import Optional, NoReturn

from sqlalchemy import select

from app.coupon.domain.coupon import Coupon
from app.coupon.exception.coupon import (
    CouponNotFoundException,
    OutOfStockException,
    AlreadyObtainException,
)
from app.user.domain.user import User
from app.user.domain.user_coupon import UserCoupon
from app.user.exception.user import UserNotFoundException
from core.db import session, Transactional, Propagation
from core.helpers.redis import redis

logger = logging.getLogger(__name__)


class CouponService:
    COUPON_COUNT = 100
    COUPON_KEY = "coupon"

    async def _get_coupon_by_id(self, coupon_id: int) -> Optional[Coupon]:
        query = (
            await session.execute(
                select(Coupon).where(Coupon.id == coupon_id),
            )
        )
        result = query.scalars().first()
        if not result:
            return

        return result

    async def _get_user_by_id(self, user_id: int) -> Optional[User]:
        query = (
            await session.execute(
                select(User).where(User.id == user_id),
            )
        )
        result = query.scalars().first()
        if not result:
            return

        return result

    @Transactional(propagation=Propagation.REQUIRED)
    async def obtain(self, coupon_id: int, user_id: int) -> Optional[NoReturn]:
        """
        Obtain coupon

        1. One user can only own one coupon for the same coupon.
        2. Coupons cannot be obtained if inventory does not exist.
        """
        user = await self._get_user_by_id(user_id=user_id)
        if not user:
            raise UserNotFoundException

        coupon = await self._get_coupon_by_id(coupon_id=coupon_id)
        if not coupon:
            raise CouponNotFoundException

        if coupon.quantity <= 0:
            raise OutOfStockException

        coupon_key = f"{self.COUPON_KEY}:{coupon_id}"
        async with redis.pipeline(transaction=True) as pipe:
            current_count, is_obtain = (
                await pipe.scard(coupon_key).sadd(coupon_key, user_id).execute()
            )

        logger.info(f"Current:: {current_count}")
        logger.info(f"is_obtain:: {is_obtain}")

        if current_count >= self.COUPON_COUNT:
            raise OutOfStockException

        if is_obtain == 0:
            raise AlreadyObtainException

        coupon.quantity = Coupon.quantity - 1
        session.add(coupon)
        user_coupon = UserCoupon(
            user=user,
            coupon=coupon,
        )
        session.add(user_coupon)
