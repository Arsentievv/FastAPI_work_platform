from pydantic import BaseModel, Field
from utils.enums import Workload
from datetime import datetime
from applicants.schemas.education_schemas import EducationGet
from applicants.schemas.experience_schemas import ExperienceGet


class ResumeBase(BaseModel):
    title: str = Field(
        max_length=256,
        description="Resume's title"
    )
    compensation: float = Field(
        gt=0,
        description="Desired compensation per month"
    )
    workload: Workload


class ResumeCreate(ResumeBase):
    worker_id: int = Field(
        gt=0,
        description="Connected worker's ID"
    )


class ResumeGet(ResumeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    educations: list["EducationGet"]
    experience: list["ExperienceGet"]