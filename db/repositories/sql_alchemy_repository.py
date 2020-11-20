import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.repository import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    @classmethod
    def session_factory(cls):

        host = os.environ.get('DB_HOST', 'localhost')
        port = 54321 if host == 'localhost' else 5432
        password = os.environ.get('DB_PASSWORD', 'abc123')
        user, db_name = 'allocation', 'allocation'
        uri = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'

        return sessionmaker(bind=create_engine(
            uri,
        ))

    def add(self, model):
        self.session.add(model)
        return model

    def list(self, model):
        return self.session.query(model)

    def commit(self):
        return self.session.commit()

    def rollback(self):
        return self.session.rollback()

    def close(self):
        return self.session.close()
