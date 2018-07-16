from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from .metro import Metro
from .stop import Stop
from .pattern import Pattern
from .route import Route

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

    def nearby_stops(self):
        radius = 0.25 # miles
        stops = Stop.objects.filter(geom__distance_lte=(self.geom, Distance(mi=radius)))
        return stops

    def nearby_patterns(self):
        stops = self.nearby_stops()
        patterns = Pattern.objects.filter(stops__in=stops).distinct()
        return patterns

    # may not even need this one for the score???
    def nearby_routes(self):
        patterns = self.nearby_patterns()
        routes = Route.objects.filter(pattern__in=patterns).distinct()
        return routes

    def get_weekly_trips(self):
        patterns = self.nearby_patterns()
        total_weekly_trips = 0
        for p in patterns:
            total_weekly_trips += p.weekly_trips
        return total_weekly_trips

    def get_frequent_trips(self):
        patterns = self.nearby_patterns()
        trips_by_route = patterns.values('route_id').annotate(
                Sum('wk_trips'),
                Sum('sa_trips'),
                Sum('su_trips'),
                Sum('wk_06_09'),
                Sum('wk_09_12'),
                Sum('wk_12_15'),
                Sum('wk_15_18'),
                Sum('wk_18_21')
            )
    #
    # def get_trips_serving_destinations(self):
    #     pass
