from django.db import models

# Create your models here.
class Activity_peroid(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

class User(models.Model):
    id = models.IntegerField(primary_key=True);
    name = models.CharField(max_length=30)
    tz = models.CharField(max_length=30)
    # activity_peroid = models.ForeignKey(Activity_peroid, on_delete=models.CASCADE)
