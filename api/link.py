

from fastapi import APIRouter

from db import unit_of_work
from models.link import Link
from pydantic import BaseModel
from services_layer.link import add_link, InvalidLink

router = APIRouter()


class LinkResponse(Link, BaseModel):
    ''' '''


@router.get('/save_for_later/{category}/{link}', response_model=LinkResponse)
def add_link_endpoint(
    category: str,
    link: str
):

    try:

        link = add_link(
            category,
            link,
            unit_of_work.UnitOfWork(),
        )

    except InvalidLink:
        return 'failed', 400

    return link
