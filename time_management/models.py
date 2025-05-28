from django.utils import timezone
from django.db import models


class Time(models.Model):
    user = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    console_time = models.IntegerField()
    computer_time = models.IntegerField()
    mobile_time = models.IntegerField()
    television_time = models.IntegerField()

    def __str__(self):
        return self.user
