FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN python manage.py migrate

CMD celery -A yourproject worker -l debug
