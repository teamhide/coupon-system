from fastapi import APIRouter, Response


coupon_router = APIRouter()


@coupon_router.post("")
async def create_coupon():
    return {}
