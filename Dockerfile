FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get clean && \
    apt-get update && \
    apt-get install -y \
    mariadb-client \
    default-libmysqlclient-dev \
    python3-dev

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt
COPY . /app/

EXPOSE 8000
