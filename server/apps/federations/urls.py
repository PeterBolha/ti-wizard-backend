from django.urls import path, include

from .routers import federations_router


urlpatterns = [
    path('', include(federations_router.urls)),
]
