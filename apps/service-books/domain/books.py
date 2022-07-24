from core.db import metadata
from sqlalchemy import Table, Column, Integer, String, Time, ForeignKey


books = Table(
    'books',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, unique=True),
    Column('author_id', Integer, ForeignKey('authors.id'), nullable=False),
    Column('title', String),
    Column('original_title', String),
    Column('year', Integer),
    Column('reading_time', Time)
)
