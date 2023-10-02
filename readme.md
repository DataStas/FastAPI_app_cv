Репозиторий для реализации сервиса моделирования пресса


План запуска для разработки:

1. Для запуска запустить docker-compose.yml (в будущем и все, а пока...)
2. Создать venv 
2.1. python3.11 -m venv venv
2.2. source ./venv/bin/activate
2.3. pip install -r requirements.txt
В конце работы не забыть:
2.4 python3 -m pip freeze > requirements.txt
2. Применение и создание миграции 
alembic upgrade "хэш миграции" 
В конце работы не забыть:
alembic revision --autogenerate -m "Database creation"
3. Запуск приложения
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload


Информация про применение инструментов
1. PostgreSS
Для хранения настроек запуска модели, информации о пользователях и результатов моделирования
2. Redis
Лежит в ОЗУ, для кэширования данных. 
Осуществляет мемоизацию (кэширование запроса) для тяжелых запросов.
Основная необходимость: оптимизировать работу преподавателя с результатами



Шаблон Данных постоянных аргументов
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
