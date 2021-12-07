"""Models for Autopark app."""
from django.db import models


class Driver(models.Model):
    """Driver model for Autopark app."""

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        """Render draver information as a string."""
        return f'{self.first_name} {self.last_name}'

class Vehicle(models.Model):
    """Vehicle model for Autopark app."""

    driver_id = models.ForeignKey(
        Driver, 
        on_delete=models.CASCADE, 
        blank=True, null=True
    )
    make = models.CharField(max_length=250)
    vehicle_model = models.CharField(max_length=250)
    plate_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        """Render vehicle information as a string."""
        return f'{self.vehicle_model} {self.plate_number}'