from django.urls import include, path

from .routers import federations_router

urlpatterns = [
    path("", include(federations_router.urls)),
]
