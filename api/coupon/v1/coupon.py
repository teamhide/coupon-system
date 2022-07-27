from fastapi import APIRouter, Request, Depends, Response, Query

from app.coupon.service.coupon import CouponService
from core.fastapi.dependencies import PermissionDependency, AllowAll

coupon_router = APIRouter()


@coupon_router.post(
    "/{coupon_id}",
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def get_coupon(
    request: Request, coupon_id: int, user_id: int = Query(None),
):
    await CouponService().obtain(
        coupon_id=coupon_id, user_id=user_id if user_id else request.user.id,
    )
    return Response(status_code=200)
