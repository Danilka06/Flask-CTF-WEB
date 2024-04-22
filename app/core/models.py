import datetime

from sqlalchemy import Column, Integer, String, DateTime, PickleType, Boolean, Date

from app.core.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    login = Column(String(30), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    points = Column(Integer, nullable=False, default=0)
    createdAt = Column(DateTime, default=datetime.datetime.now, nullable=False)

    def set_password(self, password: str):
        # TODO hash passwords
        self.password = password
        ...

    def check_password(self, password: str) -> bool:
        # TODO hash passwords
        return self.password == password
        ...