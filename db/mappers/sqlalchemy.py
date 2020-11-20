from sqlalchemy import (
    Table, MetaData, Column, Integer, String
)
from sqlalchemy.orm import mapper

from models.link import Link


metadata = MetaData()

link = Table(
    'link', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('category', String(255), nullable=False),  # make relationship
    Column('link', String(255), nullable=False)
)


def start_mappers():
    mapper(Link, link)
