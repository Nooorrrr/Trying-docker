FROM python:3.14-rc-alpine 

ENV PYTHONUNBUFFERED 1

COPY .requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdrir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
