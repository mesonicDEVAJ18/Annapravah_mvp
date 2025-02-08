from django.db import models

from django.db import models

class Donation(models.Model):
    FOOD_TYPE_CHOICES = [
        ('prepared', 'Prepared Food'),
        ('groceries', 'Groceries'),
        ('produce', 'Fresh Produce'),
    ]

    food_type = models.CharField(max_length=20, choices=FOOD_TYPE_CHOICES)
    quantity = models.FloatField()  # Quantity in kg
    expiry_date = models.DateField()
    current_location = models.CharField(max_length=255, blank=True, null=True)  # Auto-detected location
    manual_location = models.CharField(max_length=255)  # Manually entered location
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation

    def __str__(self):
        return f"{self.get_food_type_display()} - {self.quantity} kg"