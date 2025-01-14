from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domains.base_repository import BaseRepository
from app.domains.user.user import User


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session) -> None:
        super().__init__(User, db)

    def find_by_email_or_username(
        self, email: Optional[str] = None, username: Optional[str] = None
    ) -> Optional[User]:
        stmt = select(User).where(
            (User.email == email) | (User.username == username)
        )
        stmt_result = self.db.execute(stmt)
        return stmt_result.scalar()
