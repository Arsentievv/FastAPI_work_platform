from pydantic import BaseModel, Field
from datetime import date


class ExperienceBase(BaseModel):
    company_title: str = Field(
        max_length=256,
        description="Worked company name"
    )
    date_of_start: date = Field(
        description="Date of hiring"
    )
    date_of_finish: date = Field(
        description="Date of dismissal"
    )
    position: str = Field(
        description="Working position"
    )
    description: str | None = Field(
        default=None,
        description="Description of your work process"
    )


class ExperienceCreate(ExperienceBase):
    resume_id: int = Field(
        gt=0,
        description="Connected resume ID"
    )


class ExperienceGet(ExperienceBase):
    id: int