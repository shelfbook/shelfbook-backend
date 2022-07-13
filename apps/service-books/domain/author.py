from sqlalchemy.orm import relationship

from core.db import Base
from sqlalchemy import Column, Integer, String


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_year = Column(Integer)
    dead_year = Column(Integer, nullable=True)
    books = relationship("Book", back_populates="author")
