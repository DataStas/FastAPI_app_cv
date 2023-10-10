from httpx import AsyncClient


async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post("/const", json={
                                                "id": 1,
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

    assert response.status_code == 200, "Параметры не добавились"


async def test_get_specific_operations(ac: AsyncClient):
    response = await ac.get("/const", params={
        "experiment_tag": "Первый",
    })

    assert response.status_code == 200, "Параметры не прочитались"
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1