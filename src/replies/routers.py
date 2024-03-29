from fastapi import APIRouter, Depends
from replies.reply_schemas import reply_schemas
from replies.reply_crud.reply_crud import ReplyCRUD
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from companies.schemas.vacancy_schemas import VacancyGet

replies_router = APIRouter()


@replies_router.post(
    "/create_reply",
    response_model=reply_schemas.ReplyGet,
    status_code=201,
    description="Create reply"
)
async def create_reply(
        reply: reply_schemas.ReplyCreate,
        db: AsyncSession = Depends(get_session)
):
    result = ReplyCRUD.create_reply(db=db, reply=reply)
    return await result


@replies_router.get(
    "/reply/{id}",
    response_model=reply_schemas.ReplyGet,
    status_code=200,
    description="Get reply by ID"
)
async def get_reply_by_id(
        reply_id: int,
        db: AsyncSession = Depends(get_session)
):
    result = ReplyCRUD.get_reply_by_id(reply_id=reply_id, db=db)
    return await result