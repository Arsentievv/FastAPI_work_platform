from pydantic import BaseModel, Field
from datetime import date, datetime
from applicants.schemas.resume_schemas import ResumeGet


class WorkerBase(BaseModel):
    first_name: str = Field(
        max_length=256,
        description="Worker's first name"
    )
    last_name: str = Field(
        max_length=256,
        description="Worker's last name"
    )
    date_of_birth: date = Field(
        description="Worker's date of birth"
    )


class WorkerCreate(WorkerBase):
    pass


class WorkerGet(WorkerBase):
    id: int
    created_at: datetime
    updated_at: datetime


class WorkerGetWithResumes(WorkerGet):
    resumes: list[ResumeGet]