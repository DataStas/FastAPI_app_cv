Репозиторий для реализации сервиса моделирования пресса
Предполагаемый план запуска:

1. Для запуска запустить docker-compose.yml (в будущем и все, а пока...)
2. Создать venv 
2.1. python3.11 -m venv venv
2.2. source ./venv/bin/activate
2.3. pip install -r requierments.txt
2. Прогрузить миграции alembic upgrade 41ecb1a5c084
3. Проверить, что всё ок