from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from database import Base
from utils.fields import intpk, created_at, updated_at
from utils.enums import Workload, Grade
from datetime import datetime


class Worker(Base):
    __tablename__ = "workers"

    id: Mapped[intpk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    date_of_birth: Mapped[datetime]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    resumes: Mapped[list["Resume"]] = relationship(
        back_populates="workers"
    )


class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[intpk]
    title: Mapped[str]
    compensation: Mapped[float]
    workload: Mapped[Workload]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    worker_id: Mapped[int] = mapped_column(
        ForeignKey("workers.id", ondelete="CASCADE")
    )

    worker: Mapped["Worker"] = relationship(
        back_populates="resumes"
    )
    educations: Mapped[list["Education"]] = relationship(
        back_populates="resumes"
    )
    experience: Mapped[list["Experience"]] = relationship(
        back_populates="resumes"
    )
    vacancies_replied: Mapped[list["Vacancy"]] = relationship(
        back_populates="resumes_replied",
        secondary="replies"
    )


class Education(Base):
    __tablename__ = "educations"

    id: Mapped[intpk]
    organization_name: Mapped[str]
    speciality: Mapped[str]
    grade: Mapped[Grade]
    date_of_start: Mapped[datetime]
    date_of_finish: Mapped[datetime]
    resume_id: Mapped[int] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE")
    )

    resume: Mapped["Resume"] = relationship(
        back_populates="educations"
    )


class Experience(Base):
    __tablename__ = "expiriences"

    id: Mapped[intpk]
    company_title: Mapped[str]
    date_of_start: Mapped[datetime]
    date_of_finish: Mapped[datetime]
    position: Mapped[str]
    description: Mapped[str]
    resume_id: Mapped[int] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE")
    )

    resume: Mapped["Resume"] = relationship(
        back_populates="expiriences"
    )
