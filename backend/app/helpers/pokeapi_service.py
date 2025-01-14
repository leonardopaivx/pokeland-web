import random

import httpx

from app.domains.user_pokemon.user_pokemon_schema import (
    Pokemon,
    PokemonSprite,
    PokemonType,
)


async def fetch_rand_pokemon_name():
    offset = random.randint(1, 1301)

    url = f'https://pokeapi.co/api/v2/pokemon?offset={offset}&limit=1'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    return data['results'][0]['name']


async def fetch_pokemon(pokemon_identifier: str) -> Pokemon:
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_identifier.lower()}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    abilities = sorted([
        ability['ability']['name'] for ability in data['abilities']
    ])

    types = [
        PokemonType(name=pokemon_type['type']['name'])
        for pokemon_type in data['types']
    ]

    sprites = PokemonSprite(
        front_default=data['sprites'].get('front_default'),
        back_default=data['sprites'].get('back_default'),
    )

    return Pokemon(
        id=data['id'],
        name=data['name'],
        height=data['height'],
        weight=data['weight'],
        abilities=abilities,
        types=types,
        sprites=sprites,
    )
