FROM python:3.13.2-alpine

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app
COPY ./app /app

EXPOSE 8000

CMD ["sh","-c","python manage.py runserver 0.0.0.0:8000"]
