from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.contrib.gis.db.models import Collect
from django.db.models import Sum
from .metro import Metro
from .stop import Stop
from .pattern import Pattern
from .route import Route
from .destination import Destination
import csv

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

    # may not even need this one for the score?
    # def nearby_routes(self):
    #     patterns = self.nearby_patterns()
    #     routes = Route.objects.filter(pattern__in=patterns).distinct()
    #     return routes

    def get_weekly_trips(self):
        patterns = self.nearby_patterns()
        total_weekly_trips = 0
        for p in patterns:
            total_weekly_trips += p.weekly_trips
        return total_weekly_trips


    def get_frequent_trips(self):
        patterns = self.nearby_patterns()
        trips_by_route = Route.objects.values('name') \
            .filter(pattern__in=patterns) \
            .annotate(
                ampeak=Sum('pattern__wk_06_09'),
                midam=Sum('pattern__wk_09_12'),
                midpm=Sum('pattern__wk_12_15'),
                pmpeak=Sum('pattern__wk_15_18'),
                evening=Sum('pattern__wk_18_21')
            )

        frequent_trips = 0

        for r in trips_by_route:
            core_hour_trips = r["ampeak"] + r["midam"] + r["midpm"] + r["pmpeak"]
            evening_trips = r["evening"]

            # 96 trips over a 12 hour period (6am-6pm) represents an average headway of 15 minutes for bidirectional service
            # 18 trips over a 3 hour period (6pm-9pm) represents an average headway of 20 minutes for bidirectional service
            if core_hour_trips > 96 and evening_trips > 18:
                frequent_trips += core_hour_trips + evening_trips

        return frequent_trips


    def get_trips_serving_destinations(self):
        destination_set = Destination.objects.filter(metro=self.metro).aggregate(Collect("geom"))
        destination_stops = Stop.objects.filter(geom__distance_lte=(destination_set["geom__collect"], Distance(mi=0.25)))
        destination_patterns = Pattern.objects.filter(stops__in=destination_stops).distinct()

        hotel_patterns = self.nearby_patterns()

        intersect_patterns = hotel_patterns.filter(pk__in=destination_patterns)

        total_weekly_trips = 0
        for p in intersect_patterns:
            total_weekly_trips += p.weekly_trips

        return total_weekly_trips


    @classmethod
    def write_scores(cls):
        hotel_scores = []
        for h in Hotel.objects.all():
            hotel_scores.append([h.id, h.name, h.get_weekly_trips(), h.get_frequent_trips(), h.get_trips_serving_destinations()])

        new_file = open('hotel_scores.csv', 'w')
        with new_file:
            writer = csv.writer(new_file)
            writer.writerows(hotel_scores)

        return "Successful printing"
