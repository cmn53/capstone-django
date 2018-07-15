from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from .metro import Metro

class Hotel(models.Model):
    hotel_code = models.IntegerField()
    name = models.CharField(max_length=200)
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE)
    geom = models.PointField(spatial_index=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
