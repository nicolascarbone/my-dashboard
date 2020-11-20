
from db.repository import AbstractRepository


class InMemoryRepository(AbstractRepository):

    def __init__(self, session=None):
        self.data = set()

    @classmethod
    def session_factory(cls):
        # could use e = create_engine('sqlite://')
        return cls()

    def add(self, model):
        self.data.add(model.json())
        return model

    def list(self, model):
        return self.data

    def commit(self):
        return True

    def rollback(self):
        return True

    def close(self):
        return True
