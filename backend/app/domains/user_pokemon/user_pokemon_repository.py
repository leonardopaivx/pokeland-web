from sqlalchemy.orm import Session

from app.domains.base_repository import BaseRepository
from app.domains.user_pokemon.user_pokemon import UserPokemon


class UserPokemonRepository(BaseRepository[UserPokemon]):
    def __init__(self, db: Session) -> None:
        super().__init__(UserPokemon, db)
