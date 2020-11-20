
from db import unit_of_work
from models.link import Link


class InvalidLink(Exception):
    pass


def is_valid_link(link: str):
    return link != ''


def add_link(
        category: str,
        link: str,
        uow: unit_of_work.AbstractUnitOfWork
) -> Link:

    with uow:

        if not is_valid_link(link):
            raise InvalidLink('Invalid link')

        model = Link(link=link, category=category)
        _link = uow.links.add(model)

        uow.commit()

    return _link
