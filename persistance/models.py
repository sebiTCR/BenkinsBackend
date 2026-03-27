from tokenize import String

from sqlalchemy import (String, Enum)
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column


class BuildStatus:
    NONE=0,
    SUCCESS=1,
    BUILDING=2,
    FAILED=3



class Base(DeclarativeBase):
    pass


class Project(Base):
        __tablename__ = "project"

        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(30))
        version: Mapped[str] = mapped_column(String(10))
        # status: Mapped[Enum] = mapped_column(Enum("NONE", "SUCESS", "BUILDING", "FAILED", name="status_enum", create_type=True))
        status: Mapped[int] = mapped_column()

        # def __init__(self, name=None, version=None, status: int = 0):