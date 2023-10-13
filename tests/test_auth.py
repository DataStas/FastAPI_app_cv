import pytest
from sqlalchemy import insert, select

from src.auth.models import role
from conftest import client, async_session_maker


async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(role).values(id=1, name="teacher", permissions=None)
        await session.execute(stmt)
        await session.commit()

        stmt = insert(role).values(id=2, name="student", permissions=None)
        await session.execute(stmt)
        await session.commit()

        stmt = insert(role).values(id=3, name="admin", permissions=None)
        await session.execute(stmt)
        await session.commit()


        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, 'teacher', None),
                                (2, 'student', None),
                                (3, 'admin', None)], "Роли не добавились"


def test_register():
    response = client.post("/auth/register", json={
        "email": "autoemailbotss@gmail.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "Petya",
        "role_id": 1
    })

    assert response.status_code == 201