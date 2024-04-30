FROM python:3.12

RUN mkdir /pinging_service

COPY . /pinging_service

RUN chmod +x /pinging_service/docker-entrypoint.sh

RUN apt-get update
RUN apt-get install -y netcat-traditional

WORKDIR /pinging_service
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

CMD ["sh", "/pinging_service/docker-entrypoint.sh"]
