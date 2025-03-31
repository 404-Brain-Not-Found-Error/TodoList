from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class TaskStatus(str, PyEnum):
    TODO = "Cделать"
    IN_PROGRESS = "В процессе"
    DONE = "Выполнено"
    ARCHIVED = "В архиве"


class ProjectORM(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(1024))
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    tasks: Mapped[list["TasksORM"]] = relationship(back_populates="project")


class TasksORM(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(1024))
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), default=TaskStatus.TODO)
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]
    project_id: Mapped[int | None] = mapped_column(ForeignKey("projects.id"))

    project: Mapped["ProjectORM"] = relationship(back_populates="tasks")