import datetime
from typing import List

from sqlalchemy import (String, Enum, ForeignKey, JSON, DateTime)
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, MappedAsDataclass, mapped_column
from bcrypt import gensalt, hashpw

class BuildStatus:
    NONE=0,
    SUCCESS=1,
    BUILDING=2,
    FAILED=3


class Base(DeclarativeBase):
    pass


class Project(MappedAsDataclass, Base):
        __tablename__ = "project"

        builds: Mapped[List["Build"]] = relationship(init=False)
        id: Mapped[int] = mapped_column(init=False, primary_key=True)
        owner_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
        name: Mapped[str] = mapped_column(String(30))
        repo: Mapped[str] = mapped_column(String(50))
        version: Mapped[str] = mapped_column(String(10))
        type: Mapped[str] = mapped_column(String(10))
        status: Mapped[int] = mapped_column()
        path: Mapped[str] = mapped_column()


class Build(MappedAsDataclass, Base):
    __tablename__ = "build"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"))
    version: Mapped[str] = mapped_column()
    file_path: Mapped[str] = mapped_column()
    logs: Mapped[List["Log"]] = relationship(init=False)


class Log(MappedAsDataclass, Base):
    __tablename__ = "log"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    build_id: Mapped[int] = mapped_column(ForeignKey("build.id"))
    contents: Mapped[dict] = mapped_column(JSON)


class User(MappedAsDataclass, Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(30))
    projects: Mapped[List["Project"]] = relationship(init=False)
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now)
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def set_password(self, password: str):
        self.password = hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

    def check_password(self, password: str):
        return hashpw(password.encode("utf-8"), self.password.encode("utf-8")) == self.password.encode("utf-8")