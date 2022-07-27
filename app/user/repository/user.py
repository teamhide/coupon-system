from app.user.domain.user import User
from core.db import session


class UserRepo:
    async def save(self, user: User) -> None:
        session.add(user)
