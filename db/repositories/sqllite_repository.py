
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.repository import AbstractRepository


class SqlLiteRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    @classmethod
    def session_factory(cls):
        return sessionmaker(bind=create_engine('sqlite:///database.db'))()

    def add(self, model):
        self.session.add(model)
        return model

    def list(self, model):
        return self.session

    def commit(self):
        return True

    def rollback(self):
        return True

    def close(self):
        return True
