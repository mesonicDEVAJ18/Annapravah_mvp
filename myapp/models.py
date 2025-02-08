from django.db import models

class Donation(models.Model):
    FOOD_TYPE_CHOICES = [
        ('Prepared', 'Prepared Food'),
        ('Groceries', 'Groceries'),
        ('Produce', 'Fresh Produce'),
    ]

    food_type = models.CharField(max_length=20, choices=FOOD_TYPE_CHOICES)
    quantity = models.FloatField()  # Quantity in kg
    expiry_date = models.DateField()
    current_location = models.CharField(max_length=255, blank=True, null=True)  # Auto-detected location
    latitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation

    def __str__(self):
        return f"{self.get_food_type_display()} - {self.quantity} kg"


class Request(models.Model):
    FOOD_TYPE_CHOICES = Donation.FOOD_TYPE_CHOICES  # Sync with Donation model

    location = models.CharField(max_length=255, help_text="Where the food is needed")
    latitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True, help_text="Latitude of request location")
    longitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True, help_text="Longitude of request location")
    quantity = models.FloatField()  # Quantity in kg
    preferred_datetime = models.DateTimeField(help_text="Preferred date and time for delivery")
    food_type = models.CharField(max_length=20, choices=FOOD_TYPE_CHOICES, help_text="Type of food needed")
    special_instructions = models.TextField(blank=True, null=True, help_text="Any special instructions")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request for {self.quantity} people at {self.location} on {self.preferred_datetime}"