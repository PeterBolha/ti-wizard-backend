from django.db import models


class ActiveFederation(models.Model):
    url = models.URLField(unique=True)

    def __str__(self):
        return self.url
