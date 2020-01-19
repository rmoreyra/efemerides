from django.db import models
from django_extensions.db.models import TimeStampedModel

__author__ = 'rmoreyra'

class Efemerides(TimeStampedModel):
    date_efem = models.DateTimeField(null=True)
    msj_efem = models.TextField(max_length=10000, null=True)

    def get_latest(self, date_efem):
        return Efemerides.objects.filter(
            date_efem=date_efem
        ).order_by('-created').first()

