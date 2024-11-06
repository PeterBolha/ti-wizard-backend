from django.urls import include, path

from .routers import roles_router

urlpatterns = [
    path("", include(roles_router.urls)),
]
