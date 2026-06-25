from django.db import models
from events.models import Event


class Booking(models.Model):

    customer_name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    address = models.TextField()

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    SOUND_CHOICES = [
        ('2-Way', '2-Way'),
        ('3-Way', '3-Way'),
        ('Custom', 'Custom'),
    ]

    sound_type = models.CharField(
        max_length=20,
        choices=SOUND_CHOICES
    )

    custom_sound_count = models.IntegerField(
        null=True,
        blank=True
    )

    advance_payment = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    remaining_payment = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    ]

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='Pending'
    )

    def __str__(self):
        return self.customer_name