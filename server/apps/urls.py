from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("federations/", include("apps.federations.urls")),
]
