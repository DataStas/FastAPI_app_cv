from httpx import AsyncClient
from conftest import client, async_session_maker
from src.operations.models import input_const_params
from sqlalchemy import insert, select
import random

async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post("/rw_operations/const", json={
                                                            "id": 7,
                                                            "time_max": 1000,
                                                            "time_variable": 500,
                                                            "tablet_diameter": 0.011,
                                                            "tablet_height": 0.01,
                                                            "bunker_volume": 60,
                                                            "delta_force_press": 0.1,
                                                            "delta_powder_density": 0.1,
                                                            "max_pallet": 5,
                                                            "ppr_time_max": 3000,
                                                            "experiment_tag": "Первый"
                                                            })
    # response = client.post("/rw_operations/const", json={})

    assert response.status_code == 200, "Параметры не добавились"



async def test_add_role():
    async with async_session_maker() as session:
        id = random.randint(0, 10000) # !fix it after
        stmt = insert(input_const_params).values(id=id,
                                                 time_max = 1000,
                                                 time_variable = 500,
                                                 tablet_diameter = 0.011,
                                                 tablet_height = 0.01,
                                                 bunker_volume = 60,
                                                 delta_force_press = 0.1,
                                                 delta_powder_density = 0.1,
                                                 max_pallet = 5,
                                                 ppr_time_max = 3000,
                                                 experiment_tag  = "Первый")
        await session.execute(stmt)
        await session.commit()

        query = select(input_const_params)
        result = await session.execute(query)
        assert result.all() == [(7, 1000, 500, 0.011, 0.01, 60, 0.1, 0.1, 5, 3000, 'Первый'),
                                (id, 1000, 500, 0.011, 0.01, 60, 0.1, 0.1, 5, 3000, 'Первый')], "Параметры не добавились"


async def test_get_specific_operations(ac: AsyncClient):
    response = await ac.get(url="/rw_operations/const", params={"exp_tag": "Первый"})

    assert response.status_code == 200, "Параметры не прочитались"
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 2