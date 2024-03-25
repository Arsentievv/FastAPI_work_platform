from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.replies.models import Rply
from src.replies.reply_schemas import reply_schemas


class ReplyCRUD:

    @staticmethod
    async def create_reply(db: AsyncSession, reply: reply_schemas.ReplyCreate):
        reply_db = Rply(
            vacancy_id=reply.vacancy_id,
            resume_id=reply.resume_id,
            letter=reply.letter
        )
        db.add(reply_db)
        await db.commit()
        return reply_db

    @staticmethod
    async def get_reply_by_id(db: AsyncSession, reply_id: int):
        result = await db.execute(select(Rply).filter(Rply.id == reply_id))
        return result.scalar_one_or_none()