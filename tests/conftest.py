# import asyncio
# import json

# import pytest
# from sqlalchemy import insert

# from app.config import settings
# from app.database import Base, async_session_maker, engine


# @pytest.fixture(scope="session", autouse=True)
# async def create_and_populate_db():
#     print(settings.MODE)
#     assert settings.MODE == "TEST"
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)  # {{ edit_1 }}

#     def open_mock_file(filename: str):
#         with open(f"tests/{filename}.json", "r") as file:
#             return json.load(file)

#     mock_users = open_mock_file("mock_users")

#     async with async_session_maker() as session:
#         for user in mock_users:
#             add_user = insert(User).values(user)
#             await session.execute(add_user)
#             await session.commit()


# @pytest.fixture(scope="function")
# async def event_loop():
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()
#     await loop.shutdown_asyncgens()
