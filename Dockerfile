FROM python:3.9.5-slim-buster
WORKDIR /usr/src/app

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

RUN pip install --upgrade pip

COPY ./requirements-depl.txt .
RUN pip install -r requirements-depl.txt

COPY . .

CMD uvicorn app:app --reload --workers 1 --host 0.0.0.0 --port 8008
