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

    # Event Date
    event_date = models.DateField(
        null=True,
        blank=True
    )

    # Timing Choices (Morning / Evening / Full Day)
    TIMING_CHOICES = [
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
        ('Full Day', 'Full Day'),
    ]

    timing = models.CharField(
        max_length=20,
        choices=TIMING_CHOICES,
        default='Morning'
    )

    # Dholi Choices (સંખ્યા માટેના વિકલ્પો)
    DHOLI_CHOICES = [
        ('No', 'No Dholi'),
        ('2 Dholi', '2 Dholi'),
        ('4 Dholi', '4 Dholi'),
        ('6 Dholi', '6 Dholi'),
        ('8 Dholi', '8 Dholi'),
        ('Custom', 'Custom'),
    ]

    dholi = models.CharField(
        max_length=20,
        choices=DHOLI_CHOICES,
        default='No'
    )

    # Custom Dholi Count (જો 'Custom' સિલેક્ટ કરો તો આમાં એન્ટ્રી થશે)
    custom_dholi_count = models.IntegerField(
        null=True,
        blank=True
    )

    SOUND_CHOICES = [
        ('2-Way', '2-Way'),
        ('3-Way', '3-Way'),
        ('4-Way', '4-Way'),
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

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.customer_name} - {self.event_date}"