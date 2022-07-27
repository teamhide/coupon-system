from fastapi import APIRouter

from api.coupon.v1.coupon import coupon_router as coupon_v1_router
from api.user.v1.user import user_router as user_v1_router

router = APIRouter()
router.include_router(user_v1_router, prefix="/api/v1/users", tags=["User V1"])
router.include_router(
    coupon_v1_router, prefix="/api/v1/coupons", tags=["Coupon V1"],
)


__all__ = ["router"]
