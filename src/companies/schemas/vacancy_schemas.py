from pydantic import BaseModel, Field
from utils.enums import Workload
from datetime import datetime


class VacancyBase(BaseModel):
    title: str = Field(
        max_length=256,
        description="Vacancy's title"
    )
    description: str | None = Field(
        default=None,
        max_length=1024,
        description="Vacancy's description"
    )
    compensation: float = Field(
        gt=0,
        description="Compensation per month"
    )
    work_load: Workload


class VacancyCreate(VacancyBase):
    company_id: int = Field(
        gt=0,
        description="Connected company's ID"
    )


class VacancyGet(VacancyBase):
    id: int
    created_at: datetime
    updated_at: datetime