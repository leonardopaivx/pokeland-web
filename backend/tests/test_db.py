from dataclasses import asdict

from sqlalchemy import select

from app.domains.user.user import User
from app.domains.user_pokemon.user_pokemon import UserPokemon


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='leonardo', password='secret', email='teste@test'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'leonardo'))

    assert asdict(user) == {
        'id': 1,
        'username': 'leonardo',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
        'updated_at': time,
        'pokemons': [],
    }


def test_create_user_pokemon(session, user):
    user_pokemon = UserPokemon(
        user_id=user.id, pokemon_name='mew', pokemon_external_id=151
    )

    session.add(user_pokemon)
    session.commit()
    session.refresh(user_pokemon)

    user = session.scalar(select(User).where(User.id == user.id))

    assert user_pokemon in user.pokemons
