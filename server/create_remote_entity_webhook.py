import base64
import logging
import os
import secrets

import django

django.setup()

from django_webhook.models import Webhook, WebhookSecret, WebhookTopic

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("building webhook")


def generate_hmac_secret():
    random_bytes = secrets.token_bytes(32)
    secret = base64.urlsafe_b64encode(random_bytes).decode("utf-8").rstrip("=")
    return secret


webhook_url = os.getenv("WEBHOOK_URL")
webhook_secret = os.getenv("WEBHOOK_SECRET", generate_hmac_secret())
delete_previous_webhooks = os.getenv("DELETE_PREVIOUS_WEBHOOKS", True)

if not webhook_url or not webhook_secret:
    raise ValueError(
        "Both WEBHOOK_URL and WEBHOOK_SECRET environment variables must be set."
    )

if delete_previous_webhooks:
    Webhook.objects.all().delete()
    WebhookTopic.objects.all().delete()
    WebhookSecret.objects.all().delete()

# Create or update the webhook
webhook, _ = Webhook.objects.update_or_create(url=webhook_url)
webhook.save()

# Set the topics (model actions to respond to)
update_remote_entity_topic = "remote_entities.RemoteEntity/update"
created_topic = WebhookTopic.objects.create(name=update_remote_entity_topic)

topics = [created_topic]
webhook.topics.set(topics)

WebhookSecret.objects.update_or_create(webhook=webhook, token=webhook_secret)

logger.info(
    f"Webhook set to url {webhook_url} for update action on RemoteEntity model."
)
