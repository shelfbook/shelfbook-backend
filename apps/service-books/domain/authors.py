from core.db import metadata
from sqlalchemy import Table, Column, Integer, String

authors = Table(
    'authors',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, unique=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('birth_year', Integer),
    Column('dead_year', Integer)
)
