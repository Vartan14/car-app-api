from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def validate_year(value):
    if value < 1900 or value > 2024:
        raise ValidationError('Year must be between 1900 and 2024')


class Owner(models.Model):
    """Car owner model. Represents an owner of the car"""
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    """Car Model"""

    license_plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=255)
    year = models.IntegerField(validators=[validate_year])
    color = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.color} {self.brand}"



