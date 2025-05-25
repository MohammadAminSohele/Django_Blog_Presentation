FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD admin


RUN mkdir /src
WORKDIR /src

ADD Reqirments.txt /src
ADD ./volumes/src /src
RUN pip install --upgrade pip
RUN pip install -r Reqirments.txt

CMD python3 manage.py makemigrations blog account comment --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py createsuperuser --user admin --email myprogramingspace@gmail.com --noinput; \
    gunicorn -b 0.0.0.0:8000 config.wsgi