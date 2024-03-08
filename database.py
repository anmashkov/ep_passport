from sqlalchemy import create_engine

from init import DatabaseInitiator
from models import Base


class DataBase:
    def __init__(self, dsn):
        self.engine = create_engine(dsn)

    def init_database(self):
        db_init = DatabaseInitiator(Base, self.engine)
        db_init.create_tables()
