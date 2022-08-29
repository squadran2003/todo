FROM python:3.9-buster

RUN apt-get update && apt-get install nginx  -y --no-install-recommends

COPY . /app


WORKDIR /app/
RUN pip install -r requirements.txt

WORKDIR /app/todo
