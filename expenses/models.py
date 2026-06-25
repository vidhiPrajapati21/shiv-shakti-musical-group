from django.db import models
from events.models import Event


class Expense(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    EXPENSE_TYPES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Gas', 'Gas'),
        ('Chai Nasto', 'Chai Nasto'),
        ('Transport', 'Transport'),
        ('Worker Food', 'Worker Food'),
        ('Other', 'Other'),
    ]

    expense_type = models.CharField(
        max_length=50,
        choices=EXPENSE_TYPES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    expense_date = models.DateField()

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.expense_type} - ₹{self.amount}"