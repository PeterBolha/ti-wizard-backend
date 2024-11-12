from django.urls import include, path

from .routers import remote_entities_router

urlpatterns = [
    path("", include(remote_entities_router.urls)),
]
