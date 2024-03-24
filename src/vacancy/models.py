from database import Base
from fields import created_at, updated_at, intpk
from sqlalchemy.orm import Mapped, mapped_column


class Vacancy(Base):
    __tablename__ = "vacancies"

    id: Mapped[intpk]
    title: Mapped[str]
    compensation: Mapped[float]
    work_load: Mapped[]
