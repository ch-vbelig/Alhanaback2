FROM python:3.11-alpine

WORKDIR /project

ENV PYTHONDOWNWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=11

COPY . .

RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev && \
    pip install --no-cache-dir -r requirements.txt

