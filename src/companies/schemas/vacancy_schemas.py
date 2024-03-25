from pydantic import BaseModel
from utils.enums import Workload
from datetime import datetime


class VacancyBase(BaseModel):
    title: str
    compensation: float
    work_load: Workload


class VacancyCreate(VacancyBase):
    company_id: int


class VacancyGet(VacancyBase):
    id: int
    created_at: int
    updated_at: int