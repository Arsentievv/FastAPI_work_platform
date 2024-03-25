from pydantic import BaseModel
from datetime import date, datetime
from applicants.schemas.resume_schemas import ResumeGet


class WorkerBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date


class WorkerCreate(WorkerBase):
    pass


class WorkerGet(WorkerBase):
    id: int
    created_at: datetime
    updated_at: datetime


class WorkerGetWithResumes(WorkerGet):
    resumes: list[ResumeGet]