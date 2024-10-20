from django.db import models


class ActiveFederation(models.Model):
    federation_id = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.federation_id
