from core import config

import databases
from sqlalchemy import create_engine, MetaData

database = databases.Database(config.DATABASE_URL)
metadata = MetaData()
engine = create_engine(config.DATABASE_URL)

metadata.create_all(bind=engine)
