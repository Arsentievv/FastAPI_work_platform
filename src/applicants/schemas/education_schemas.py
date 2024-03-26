from pydantic import BaseModel, Field
from datetime import date
from utils.enums import Grade


class EducationBase(BaseModel):
    organization_name: str = Field(
        max_length=256,
        min_length=3,
        description="Education organization name"
    )
    speciality: str = Field(
        max_length=256,
        description="Acquired qualification"
    )
    grade: Grade = Field(
        description="Education grade"
    )
    date_of_start: date = Field(
        description="Date of start"
    )
    date_of_finish: date = Field(
        description="Graduation date"
    )


class EducationCreate(EducationBase):
    # resume_id: int = Field(
    #     gt=0,
    #     description="Connected resume ID"
    # )
    pass
    

class EducationGet(EducationBase):
    id: int

