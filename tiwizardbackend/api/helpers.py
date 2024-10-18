from pymongo.collection import Collection

from django.conf import settings

# This import works despite being flagged by the editor
from tiwizardbackend.settings import MONGO_DB


def get_collection(name: str) -> Collection:
    return MONGO_DB[name]
