FROM python:3.11.3-alpine3.17

COPY . /app
WORKDIR /app
ENV PATH="/root/.local/bin:${PATH}"

RUN apk update && apk upgrade && \
    apk add curl &&\
    curl -sSL https://install.python-poetry.org | python3 - && \
    poetry install