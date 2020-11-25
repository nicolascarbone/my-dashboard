
from db.repositories.sql_alchemy_repository import SqlAlchemyRepository

BASE_REPOSITORY = SqlAlchemyRepository

DEFAULT_SESSION_FACTORY = BASE_REPOSITORY.session_factory

from db.mappers.sqlalchemy import start_mappers
DB_MAPPER = start_mappers
