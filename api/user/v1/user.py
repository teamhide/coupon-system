from fastapi import APIRouter, Response

from api.user.v1.request.user import CreateUserRequest
from app.user.service.user import UserService

user_router = APIRouter()


@user_router.post("")
async def create_user(request: CreateUserRequest):
    await UserService().create(name=request.name, password=request.password)
    return Response(status_code=200)

