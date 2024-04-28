FROM python:3.12

RUN mkdir /celery_service

COPY . /celery_service

RUN chmod +x /celery_service/docker-entrypoint.sh

RUN apt-get update
RUN apt-get install -y postgresql-client

WORKDIR /celery_service
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-dev


ENTRYPOINT ["/celery_service/docker-entrypoint.sh"]

CMD ["celery", "worker"]
