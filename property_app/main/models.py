from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50, choices=[
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
    ])
    status = models.CharField(max_length=50, choices=[
        ('Available', 'Available'),
        ('Sold', 'Sold'),
    ])

    def __str__(self):
        return self.name
