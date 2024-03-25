from pydantic import BaseModel, Field
from datetime import datetime


class ReplyBase(BaseModel):
    letter: str | None = Field(
        default=None,
        max_length=1024,
        description="Covering letter"
    )
    vacancy_id: int = Field(
        gt=0,
        description="Connected vacancy's  ID"
    )
    resume_id: int = Field(
        gt=0,
        description="Connected resume's ID"
    )


class ReplyCreate(ReplyBase):
    pass


class ReplyGet(ReplyBase):
    id: int
    created_at: datetime
    updated_at: datetime
