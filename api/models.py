# api/models.py
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    doctor = models.CharField(max_length=150)
    date = models.DateField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.doctor} ({self.date})"


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.full_name
