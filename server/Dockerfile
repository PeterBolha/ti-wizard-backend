# Dockerfile
FROM python:3.12-slim

# Install the required packages
RUN mkdir /server && apt-get update && pip install poetry && poetry config virtualenvs.create false

# Set the working directory in the container
WORKDIR /server


COPY ./server/pyproject.toml /server/

# Install the dependencies
RUN python3 -m poetry install

# Copy the rest of the application code into the container
COPY ./server /server/


# Set environment variable for Django settings module
ENV DJANGO_SETTINGS_MODULE=config.settings

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["sh", "-c", "python3 ./manage.py migrate && python3 ./manage.py runserver 0.0.0.0:8000"]