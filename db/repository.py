import abc


class AbstractRepository(abc.ABC):

    def __init__(self, session):
        self.session = session

    @classmethod
    @abc.abstractmethod
    def session_factory(cls):
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, model):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self, model):
        raise NotImplementedError

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError

    @abc.abstractmethod
    def close(self):
        raise NotImplementedError
