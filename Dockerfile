FROM python:3.11
LABEL authors="eldiyar"
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
WORKDIR /CarRacing

COPY requirements.txt /CarRacing

RUN pip install --upgrade pip
RUN pip install -r /CarRacing/requirements.txt
COPY . /CarRacing