from fastapi import APIRouter, Request, Depends, Response

from app.coupon.service.coupon import CouponService
from core.fastapi.dependencies import PermissionDependency, IsAuthenticated

coupon_router = APIRouter()


@coupon_router.post(
    "",
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def get_coupon(request: Request):
    await CouponService().get_coupon(user_id=request.user.id)
    return Response(status_code=200)
