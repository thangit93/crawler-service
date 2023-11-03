FROM python:3.12.0-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY poetry.lock /app
COPY pyproject.toml /app/
RUN apk add curl && curl -sSL https://install.python-poetry.org | python3.12 - --preview  && \
    /root/.local/bin/poetry export --without-hashes -f requirements.txt --output requirements.txt && \
    /usr/local/bin/python -m pip install --upgrade pip pip==23.3.1 && \
    pip install -r requirements.txt
ENV PATH="${PATH}:/root/.local/bin"
EXPOSE 5000
COPY . /app
