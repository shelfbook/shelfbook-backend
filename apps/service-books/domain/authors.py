from datetime import datetime

from core.db import metadata
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ColumnDefault
from sqlalchemy.schema import FetchedValue

authors = Table(
    'authors',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, unique=True),
    Column('first_name', String(64)),
    Column('middle_name', String(64), nullable=True, server_default=None),
    Column('last_name', String(64)),
    Column('birth_year', Integer),
    Column('dead_year', Integer),
    Column('is_confirmed', Boolean, server_default="false"),
    Column('is_processed', Boolean, server_default="false"),
    Column('created_at', DateTime, default=datetime.now),
    Column('updated_at', DateTime, onupdate=datetime.now, default=datetime.now)
)
