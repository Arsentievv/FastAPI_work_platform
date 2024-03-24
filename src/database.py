from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from config import get_settings
from sqlalchemy.orm import DeclarativeBase

settings = get_settings()

engine = create_async_engine(
    url=settings.postgres.database_url_asyncpg,
    echo=True
)


class Base(DeclarativeBase):
    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f'{col} = {getattr(self, col)}')
        return f"<{self.__class__.__name__} {','.join(cols)}>"


async def get_session() -> AsyncSession:
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
