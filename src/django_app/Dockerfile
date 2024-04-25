FROM python:3.12

RUN mkdir /django_app

COPY . /django_app

RUN ls -la /django_app
RUN chmod +x /django_app/docker-entrypoint.sh
RUN ls -la /django_app/docker-entrypoint.sh

RUN apt-get update
RUN apt-get install -y postgresql-client

WORKDIR /django_app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-dev


CMD ["sh", "/django_app/docker-entrypoint.sh"]
