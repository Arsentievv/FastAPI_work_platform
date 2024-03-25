from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from utils.fields import intpk, updated_at, created_at
from database import Base


class Rply(Base):
    __tablename__ = "replies"

    id: Mapped[intpk]
    resume_id: Mapped[int] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE"),
        primary_key=True
    )
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancies.id", ondelete="CASCADE"),
        primary_key=True
    )
    letter: Mapped[str | None]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]