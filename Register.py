from config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, MYSQL_HOST, MYSQL_PORT
from database import DataBase


class Register:

    instance = None

    def __init__(self):
        self.db = None
        self.yd = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def get_db(self):
        if self.db is None:
            dsn = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
            self.db = DataBase(dsn)

        return self.db


register = Register()