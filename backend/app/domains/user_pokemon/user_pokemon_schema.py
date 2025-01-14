from typing import List, Optional

from pydantic import BaseModel


class PokemonType(BaseModel):
    name: str
    url: Optional[str] = None


class PokemonSprite(BaseModel):
    front_default: Optional[str]
    back_default: Optional[str]


class Pokemon(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    abilities: List[str]
    types: List[PokemonType]
    sprites: PokemonSprite
