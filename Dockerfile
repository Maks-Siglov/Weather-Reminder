FROM python:3.11-alpine3.15

COPY requirements/prod.txt /temp/requirements.txt
COPY weather_reminder /weather_reminder

WORKDIR /weather_reminder
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser -D -H myuser

USER myuser
