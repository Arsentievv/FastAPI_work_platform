from pydantic import BaseModel
from datetime import datetime


class ReplyBase(BaseModel):
    letter: str | None = None
    vacancy_id: int
    resume_id: int


class ReplyCreate(ReplyBase):
    pass


class ReplyGet(ReplyBase):
    id: int
    created_at: datetime
    updated_at: datetime
