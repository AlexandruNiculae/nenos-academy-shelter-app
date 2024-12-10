FROM python:3.10

RUN mkdir /app
WORKDIR /app

RUN mkdir src
COPY src src

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/
RUN poetry install -n --no-root

EXPOSE 8050
EXPOSE 8080
# ENTRYPOINT ["python3", "/app/src/main.py"]