from datetime import datetime

from core.db import metadata
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime

authors = Table(
    'authors',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, unique=True),
    Column('first_name', String(64)),
    Column('middle_name', String(64), nullable=True, default=None),
    Column('last_name', String(64)),
    Column('birth_year', Integer),
    Column('dead_year', Integer),
    Column('is_confirmed', Boolean, default=False),
    Column('is_processed', Boolean, default=False),
    Column('created_at', DateTime, default=datetime.now),
    Column('updated_at', DateTime, onupdate=datetime.now)
)
