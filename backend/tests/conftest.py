from contextlib import contextmanager
from datetime import datetime

import pytest
from sqlalchemy import StaticPool, create_engine, event
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from app.config.db import table_registry
from app.domains.user.user import User
from app.main import create_app


@contextmanager
def _mock_db_time(*, model, time=datetime(2024, 1, 1)):
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = time
            target.updated_at = time

    event.listen(model, 'before_insert', fake_time_hook)

    yield time

    event.remove(model, 'before_insert', fake_time_hook)


@pytest.fixture
def engine():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)
    return engine


@pytest.fixture
def app(engine):
    app = create_app(engine)
    app.config.update({
        'TESTING': True,
    })

    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def session(engine):
    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def mock_db_time():
    return _mock_db_time


@pytest.fixture
def user(session):
    user = User(
        username='Teste',
        email='teste@test.com',
        password=generate_password_hash('testtest'),
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    yield user

    session.delete(user)
    session.commit()
