import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.federations.models import ActiveFederation


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_create_federation(api_client):
    url = reverse('api:federations-list')
    data = {"url": "https://federation.example.com"}
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert ActiveFederation.objects.count() == 1
    assert ActiveFederation.objects.get().url == data['url']


@pytest.mark.django_db
def test_delete_federation(api_client):
    federation = ActiveFederation.objects.create(url="https://federation.example.com")
    url = reverse('api:federations-detail', args=[federation.id])
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert ActiveFederation.objects.count() == 0
