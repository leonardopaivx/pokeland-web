from sqlalchemy import create_engine
from sqlalchemy.orm import registry

from app.config.settings import Settings

table_registry = registry()

engine = create_engine(Settings().DB_URL)
