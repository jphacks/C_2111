<<<<<<< HEAD
FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

COPY poetry.lock pyproject.toml ./
COPY goo_lab accounts django_pjt django_app onnx_model templates ./
COPY static .gitignore manage.py db.sqlite3 graph ./
# Git のインストール
RUN apt-get update && apt-get -y install git
RUN apt-get install gcc -y
RUN apt-get install g++ -y
RUN apt-get install curl -y
RUN apt-get install fonts-mplus -y
RUN pip install gunicorn
RUN pip install --upgrade pip

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN pip install poetry

# Poetry で導入したパッケージ(pyproject.toml)を全てインストール
RUN poetry config virtualenvs.create false \
  && poetry install

CMD python3 manage.py makemigrations
CMD python3 manage.py migrate
CMD gunicorn django_pjt.wsgi:application --bind 0.0.0.0:$PORT
=======
FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

COPY poetry.lock pyproject.toml ./

# Git のインストール
RUN apt-get update && apt-get -y install git
RUN apt-get install gcc -y
RUN apt-get install g++ -y
RUN apt-get install curl -y
RUN apt-get install fonts-mplus -y
RUN pip install --upgrade pip

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN pip install poetry

# Poetry で導入したパッケージ(pyproject.toml)を全てインストール
RUN poetry config virtualenvs.create false \
  && poetry install

>>>>>>> b7cd7e9d01843d2cef27f693058c3d70cd6257d8
