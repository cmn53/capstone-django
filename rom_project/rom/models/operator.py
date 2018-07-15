from django.contrib.gis.db import models
from .metro import Metro

class Operator(models.Model):
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    operator_onestop_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name
