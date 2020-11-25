

from project.config import BASE_REPOSITORY
from dataclasses import dataclass


@dataclass
class Link:
    link: str
    category: str


class LinkDatabaseRepository(BASE_REPOSITORY):
    ''' '''

    def get_links_by_category(self):
        ...
