from django.db import models


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

    def __str__(self):
        return f"№{self.pk} | {self.first_name} {self.last_name}"


class Car(models.Model):
    """Car Model"""
    license_plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=255)
    year = models.IntegerField()
    color = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.color} {self.brand}"
