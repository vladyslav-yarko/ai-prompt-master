from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
