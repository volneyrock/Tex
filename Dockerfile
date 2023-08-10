FROM python:alpine3.18

WORKDIR /app

RUN apk update && \
    apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    postgresql-dev \
    python3-dev \
    jpeg-dev \
    zlib-dev \
    libjpeg

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip

# Install Poetry and project dependencies
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . /app/

ENTRYPOINT ["poetry", "run"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
