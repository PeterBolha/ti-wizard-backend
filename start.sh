#!/bin/sh

# Run migrations and create superuser
python3 ./manage.py migrate
python3 /server/create_superuser.py --email=real.mail@gmail.com

# Start the server in the background
python3 ./manage.py runserver 0.0.0.0:8000 &

# Wait for the server to be ready
echo "Waiting for the server to start..."
until curl -s http://0.0.0.0:8000 > /dev/null; do
    sleep 1
done
echo "Server is up!"

# Create the webhook
echo "Creating remote entity webhook..."
python3 /server/create_remote_entity_webhook.py || { echo "Webhook creation failed"; exit 1; }

# Keep the container running
wait
