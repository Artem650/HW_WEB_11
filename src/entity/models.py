from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = 'contacts'
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50), index=True)
    lastname: Mapped[str] = mapped_column(String(50), index=True)
    email: Mapped[str] = mapped_column(String(50), index=True)
    phone: Mapped[str] = mapped_column(String(25))
    birthday: Mapped[Date] = mapped_column(Date, index=True)
    completed: Mapped[bool] = mapped_column(default=False)