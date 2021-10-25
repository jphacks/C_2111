FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

COPY poetry.lock pyproject.toml ./

# Git のインストール
RUN apt-get update && apt-get -y install git
RUN apt-get install build-essential -y
RUN apt-get install curl -y
RUN pip install --upgrade pip

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN pip install poetry

# Poetry で導入したパッケージ(pyproject.toml)を全てインストール
RUN poetry config virtualenvs.create false \
  && poetry install

