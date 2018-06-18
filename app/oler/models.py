from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    is_rider = models.BooleanField('Rider', default=False)
    is_driver = models.BooleanField('Driver', default=False)


class RideHistory(models.Model):

    SHARE = 1
    MINI_GO = 2
    RIDE_TYPE = (
        (SHARE, 'share'),
        (MINI_GO, 'mini_go'),
    )
    driver = models.ForeignKey(User, related_name="driver", on_delete=models.CASCADE, blank=True, null=True)
    ride_type = models.IntegerField(default=MINI_GO, choices=RIDE_TYPE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RideTrack(models.Model):

    REQUESTED = 1
    ACCEPTED = 2
    ONGOING = 3
    COMPLETED = 4
    REJECTED = 5
    RIDE_STATE = (
        (REQUESTED, 'requested'),
        (ACCEPTED, 'accepted'),
        (ONGOING, 'ongoing'),
        (COMPLETED, 'completed'),
        (REJECTED, 'rejected'),
    )
    ride_state = models.IntegerField(default=0, choices=RIDE_STATE)
    history = models.ForeignKey(RideHistory, related_name="history", on_delete=models.CASCADE, blank=True, null=True)
    rider = models.ForeignKey(User, related_name="rider", on_delete=models.CASCADE, blank=True, null=True)
    seats = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
