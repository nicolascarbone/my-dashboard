# import os

# from db.repositories.sql_alchemy_repository import SqlAlchemyRepository
# from db.repositories.in_memory_repository import InMemoryRepository
# from db.mappers.in_memory import start_mappers
from db.repositories.sqllite_repository import SqlLiteRepository

BASE_REPOSITORY = SqlLiteRepository

DEFAULT_SESSION_FACTORY = BASE_REPOSITORY.session_factory

from db.mappers.sqlalchemy import start_mappers
DB_MAPPER = start_mappers
