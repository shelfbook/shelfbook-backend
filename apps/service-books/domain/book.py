from sqlalchemy import Column, Integer, String, Time
from sqlalchemy.orm import relationship

from core.db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    author = relationship("Author", back_populates="books")
    title = Column(String)
    original_title = Column(String)
    year = Column(Integer)
    # genre =
    reading_time = Column(Time)
