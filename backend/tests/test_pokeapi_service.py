import pytest
from httpx import AsyncClient

from app.domains.user_pokemon.user_pokemon_schema import Pokemon
from app.helpers.pokeapi_service import fetch_pokemon, fetch_rand_pokemon_name


@pytest.mark.asyncio
async def test_fetch_pokemon(monkeypatch):
    MOCK_RESPONSE = {
        'id': 25,
        'name': 'pikachu',
        'height': 4,
        'weight': 60,
        'abilities': [
            {
                'ability': {
                    'name': 'static',
                    'url': 'https://pokeapi.co/api/v2/ability/9/',
                }
            },
            {
                'ability': {
                    'name': 'lightning-rod',
                    'url': 'https://pokeapi.co/api/v2/ability/31/',
                }
            },
        ],
        'types': [
            {
                'type': {
                    'name': 'electric',
                    'url': 'https://pokeapi.co/api/v2/type/13/',
                }
            }
        ],
        'sprites': {
            'front_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png',
            'back_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png',
        },
    }

    # Simulando a resposta da API
    async def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self):
                pass

            def json(self):  # noqa: PLR6301
                return MOCK_RESPONSE

        return MockResponse()

    # Substituindo o método get do AsyncClient pelo mock
    monkeypatch.setattr(AsyncClient, 'get', mock_get)

    pokemon = await fetch_pokemon('pikachu')

    # Verificando se os dados retornados estão corretos
    assert isinstance(pokemon, Pokemon)
    assert pokemon.id == 25  # noqa: PLR2004
    assert pokemon.name == 'pikachu'
    assert pokemon.height == 4  # noqa: PLR2004
    assert pokemon.weight == 60  # noqa: PLR2004
    assert pokemon.abilities == [
        'lightning-rod',
        'static',
    ]
    assert pokemon.types[0].name == 'electric'
    assert (
        pokemon.sprites.front_default
        == 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png'
    )
    assert (
        pokemon.sprites.back_default
        == 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png'
    )


async def test_fetch_rand_pokemon_name(monkeypatch):
    MOCK_RESPONSE = {
        'count': 1126,
        'next': None,
        'previous': None,
        'results': [
            {
                'name': 'bulbasaur',
                'url': 'https://pokeapi.co/api/v2/pokemon/1/',
            }
        ],
    }

    # Função mock que substitui o método `get` do `AsyncClient`
    async def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self):
                pass

            def json(self):  # noqa: PLR6301
                return MOCK_RESPONSE

        return MockResponse()

    # Substituindo o método get pelo mock
    monkeypatch.setattr(AsyncClient, 'get', mock_get)

    # Executando o método com o mock
    pokemon_name = await fetch_rand_pokemon_name()

    # Verificando o resultado
    assert pokemon_name == 'bulbasaur'
