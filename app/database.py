from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from .database import settings

if settings.MODE == "TEST":
    DATABASE_PARAM: dict = {"poolclass": NullPool}
    DATABASE_URL: str = settings.TEST_DB_URL
else:
    DATABASE_PARAM: dict = {}
    DATABASE_URL: str = settings.DB_URL

engine = create_async_engine(DATABASE_URL, **DATABASE_PARAM)
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass
