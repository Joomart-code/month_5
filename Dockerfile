FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1 

WORKDIR /shop


COPY requirements.txt /shop/requirements.txt


RUN pip install -r /shop/requirements.txt

COPY . .

