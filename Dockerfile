# FROM python:3.11-slim

# # set the working directory
# WORKDIR /press

# # install dependencies
# COPY ./requirements.txt ./
# RUN pip install --no-cache-dir --upgrade -r requirements.txt
# # copy the src to the folder
# COPY ./src ./src

# # start the server
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

FROM python:3.11

RUN mkdir /press

WORKDIR /press

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

# COPY ./docker .

# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# RUN chmod a+x docker/*.sh

# CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 --reload