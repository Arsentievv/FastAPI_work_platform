from pydantic import BaseModel
from datetime import date


class ExperienceBase(BaseModel):
    company_title: str
    date_of_start: date
    date_of_finish: date
    position: str
    description: str


class ExperienceCreate(ExperienceBase):
    resume_id: int


class ExperienceGet(ExperienceBase):
    id: int