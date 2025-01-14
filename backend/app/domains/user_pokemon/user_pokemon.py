from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.db import table_registry

if TYPE_CHECKING:
    from app.domains.user.user import User


@table_registry.mapped_as_dataclass
class UserPokemon:
    __tablename__ = 'user_pokemons'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'), nullable=False
    )

    pokemon_name: Mapped[str] = mapped_column(nullable=False)
    pokemon_external_id: Mapped[int] = mapped_column(nullable=False)

    user: Mapped['User'] = relationship(
        'User', init=False, back_populates='pokemons'
    )

    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
