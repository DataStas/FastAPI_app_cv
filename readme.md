Репозиторий для реализации сервиса моделирования пресса
Предполагаемый план запуска:

1. Для запуска запустить docker-compose.yml (в будущем и все, а пока...)
2. Создать venv 
2.1. python3.11 -m venv venv
2.2. source ./venv/bin/activate
2.3. pip install -r requirements.txt
В конце работы
2.4 python3 -m pip freeze > requirements.txt
2. Миграции 
alembic upgrade "хэш миграции" 
alembic revision --autogenerate -m "Database creation"
3. Проверить, что всё ок 
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload


{
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
}
