from django.db import models


class Time(models.Model):
    console_time = models.IntegerField()
    pc_time = models.IntegerField()
    mobile_time = models.IntegerField()
    television_time = models.IntegerField()

    def __str__(self):
        return self.mobile_time
