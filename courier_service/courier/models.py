from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username

class Parcel(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('will_reach_soon', 'Will Reach Soon'),
        ('collected', 'Collected'),
        ('started_journey', 'Started Journey'),
        ('will_arrive_soon', 'Will Arrive Soon'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=100)
    sender_address = models.TextField()
    receiver_name = models.CharField(max_length=100)
    receiver_address = models.TextField()
    receiver_phone = models.CharField(max_length=15)
    description = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Parcel {self.id} - {self.sender_name} to {self.receiver_name}"

class Tracking(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE, related_name='trackings')
    status = models.CharField(max_length=20, choices=Parcel.STATUS_CHOICES)
    location = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tracking {self.parcel.id} - {self.status} at {self.timestamp}"
