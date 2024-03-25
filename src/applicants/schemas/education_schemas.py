from pydantic import BaseModel
from datetime import date
from utils.enums import Grade


class EducationBase(BaseModel):
    organization_name: str
    speciality: str
    grade: Grade
    date_of_start: date
    date_of_finish: date


class EducationCreate(EducationBase):
    resume_id: int
    

class EducationGet(EducationBase):
    id: int

