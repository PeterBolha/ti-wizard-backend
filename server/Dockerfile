# Dockerfile
FROM python:3.12-slim

# Install the required packages
RUN mkdir /server && apt-get update && pip install poetry && poetry config virtualenvs.create false

# Set the working directory in the container
WORKDIR /server

# Copy the rest of the application code into the container
COPY ./server /server/

# Install the dependencies
RUN poetry lock --no-update && poetry install && poetry update

# Set environment variable for Django settings module
ENV DJANGO_SETTINGS_MODULE=config.settings

# Expose the port the app runs on
EXPOSE 8000

# Install curl for the startscript to check if the server is alraedy up
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Run the application
COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["sh", "/start.sh"]