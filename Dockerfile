FROM python:3.12

RUN mkdir /src

COPY ./src /src
RUN apt-get update
RUN apt-get install -y postgresql-client

WORKDIR /src
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

CMD ["./docker-entrypoint.sh"]
