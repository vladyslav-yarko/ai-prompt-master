from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
    
# I need to separate field from base because of repository logic and secondary tables

class BaseFields:
    # I also i wanted to use uuid as primary key
    # id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    id: Mapped[int] = mapped_column(primary_key=True)
    
    createdAt: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updatedAt: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
