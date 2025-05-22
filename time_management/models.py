from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Time(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    console_time = models.IntegerField()
    computer_time = models.IntegerField()
    mobile_time = models.IntegerField()
    television_time = models.IntegerField()

    def __str__(self):
        return self.mobile_time
