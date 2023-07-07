from django.db import models
from django.contrib.auth.models import User

class Sensor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sensor_set')
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    counter = models.FloatField(default=20.0)
    token = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def str(self):
        return self.name