from database import Base
from utils.fields import intpk, updated_at, created_at
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.enums import Workload


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[intpk]
    title: Mapped[str]
    information: Mapped[str | None]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    vacancies: Mapped[list["Vacancy"]] = relationship(
        back_populates="company"
    )


class Vacancy(Base):
    __tablename__ = "vacancies"

    id: Mapped[intpk]
    title: Mapped[str]
    compensation: Mapped[float]
    work_load: Mapped[Workload]
    description: Mapped[str | None]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id", ondelete="CASCADE")
    )

    company: Mapped["Company"] = relationship(
        back_populates="vacancies"
    )

    resumes_replied: Mapped[list["Resume"]] = relationship(
        back_populates="vacancies_replied",
        secondary="replies",
    )
