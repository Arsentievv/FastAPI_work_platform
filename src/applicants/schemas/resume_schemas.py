from pydantic import BaseModel
from utils.enums import Workload
from datetime import datetime
from applicants.schemas.education_schemas import EducationGet
from applicants.schemas.experience_schemas import ExperienceGet


class ResumeBase(BaseModel):
    title: str
    compensation: float
    workload: Workload


class ResumeCreate(ResumeBase):
    worker_id: int


class ResumeGet(ResumeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    educations: list["EducationGet"]
    experience: list["ExperienceGet"]