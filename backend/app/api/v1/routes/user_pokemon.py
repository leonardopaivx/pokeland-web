from asyncio import gather

from flask import Blueprint, g

from app.domains.user.user import User
from app.domains.user_pokemon.user_pokemon import UserPokemon
from app.domains.user_pokemon.user_pokemon_repository import (
    UserPokemonRepository,
)
from app.helpers import security
from app.helpers.pokeapi_service import fetch_pokemon, fetch_rand_pokemon_name

user_pokemon_bp = Blueprint(
    'user_pokemon', __name__, url_prefix='/user-pokemons'
)


@user_pokemon_bp.post('/catch')
@security.async_token_required
async def catch_pokemon(current_user: User):
    pokemon_name = await fetch_rand_pokemon_name()

    pokemon = await fetch_pokemon(pokemon_name)

    user_pokemon_repository = UserPokemonRepository(g.db_session)
    user_pokemon = UserPokemon(
        user_id=current_user.id,
        pokemon_name=pokemon.name,
        pokemon_external_id=pokemon.id,
    )
    user_pokemon_repository.create(user_pokemon)

    return pokemon.model_dump_json()


@user_pokemon_bp.get('')
@security.async_token_required
async def list_user_pokemons(current_user: User):
    user_pokemons = current_user.pokemons

    fetched_pokemons = await gather(
        *(fetch_pokemon(user_pokemon) for user_pokemon in user_pokemons)
    )

    return [pokemon.model_dump_json() for pokemon in fetched_pokemons]
