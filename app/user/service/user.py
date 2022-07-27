from app.user.domain.user import User
from app.user.repository.user import UserRepo
from core.db import Transactional, Propagation


class UserService:
    def __init__(self):
        self.user_repo = UserRepo()

    @Transactional(propagation=Propagation.REQUIRED)
    async def create(self, name: str, password: str) -> None:
        user = User.create(name=name, password=password)
        await self.user_repo.save(user=user)
