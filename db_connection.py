import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

load_dotenv()
DATABASE_URL = f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:5432/{os.getenv('POSTGRES_DB')}"

engine = create_async_engine(DATABASE_URL)
new_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autocommit=False,
)


async def get_session():
    async with new_session() as session:
        yield session
