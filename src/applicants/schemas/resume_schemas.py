from pydantic import BaseModel, Field
from utils.enums import Workload
from datetime import datetime
from applicants.schemas.education_schemas import EducationGet, EducationCreate
from applicants.schemas.experience_schemas import ExperienceGet, ExperienceCreate


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
    worker_id: int = Field(
        gt=0,
        description="Connected worker's ID"
    )


class ResumeCreate(ResumeBase):
    educations: list["EducationCreate"] | None
    experiences: list["ExperienceCreate"] | None
    pass


class ResumeGet(ResumeBase):
    id: int
    created_at: datetime
    updated_at: datetime


class ResumeWithConnections(ResumeGet):
    educations: list["EducationGet"] | None
    experiences: list["ExperienceGet"] | None
