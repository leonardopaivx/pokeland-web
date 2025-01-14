from typing import Generic, List, Optional, Type, TypeVar

from sqlalchemy import select, update
from sqlalchemy.orm import Session

T = TypeVar('T')


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], db: Session) -> None:
        self.model = model
        self.db = db

    def create(self, entity: T) -> None:
        self.db.add(entity)
        self.db.commit()

    def update(self, entity: T) -> None:
        stmt = (
            update(self.model)
            .where(self.model.id == entity.id)
            .values(**entity.__dict__)
        )
        self.db.execute(stmt)
        self.db.commit()

    def all(self) -> List[T]:
        stmt = select(self.model)
        stmt_result = self.db.execute(stmt)
        return stmt_result.scalars().all()

    def find(self, id: str) -> Optional[T]:
        stmt = select(self.model).where(self.model.id == id)
        stmt_result = self.db.execute(stmt)
        return stmt_result.scalar()
