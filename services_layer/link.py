
from db import unit_of_work
from models.link import Link


def add_link(
        category: str,
        link: str,
        uow: unit_of_work.AbstractUnitOfWork
) -> Link:

    with uow:

        model = Link(link=link, category=category)
        link_instance = uow.links.add(model)

        uow.commit()

    return link_instance
