FROM python:3.10

RUN mkdir /app
WORKDIR /app

RUN mkdir src
COPY src src
RUN mkdir test
COPY test test

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/
RUN poetry install -n --no-root

ENV PYTHONPATH="/app/src:${PYTHONPATH}"

WORKDIR /app/src

EXPOSE 8050
EXPOSE 8080
# ENTRYPOINT ["python3", "./api/main.py"]