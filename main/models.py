from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    tz = models.CharField(max_length=30)


class Activity_peroid(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)