from django.db import models

# Create your models here.
from django.db import models


class Event(models.Model):

    EVENT_TYPES = [
        ('Wedding', 'Wedding'),
        ('Haldi','Haldi'),
        ('school Function','school Function'),
        ('Birthday', 'Birthday'),
        ('Garba', 'Garba'),
        ('Corporate', 'Corporate'),
        ('DJ Night', 'DJ Night'),
        ('Barat on wheels','Barat on wheels'),
        ('Other', 'Other'),
    ]
    event_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPES
    )

    def __str__(self):
        return self.event_type