# Dockerfile
FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Copy dependencies
COPY requirements.txt /code/

# Upgrade pip
RUN pip install --upgrade pip

# Install packages
RUN pip install django-cors-headers

# Install required dependencies
RUN pip install -r requirements.txt


COPY . /code/