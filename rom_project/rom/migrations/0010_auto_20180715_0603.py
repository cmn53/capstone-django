# Generated by Django 2.0.7 on 2018-07-15 06:03

import json
from django.db import migrations
from django.contrib.gis.db import models
from django.contrib.gis.geos import LineString, MultiLineString, GEOSGeometry


def load_route_data(apps, schema_editor):
    Operator = apps.get_model('rom', 'Operator')
    Route = apps.get_model('rom', 'Route')

    with open('rom/fixtures/route_data.json') as json_file:
        data = json.load(json_file)

        for d in data:
            try:
                lines = []
                for l in d["geometry"]:
                    line = LineString(l)
                    lines.append(line)

                operator = Operator.objects.get(operator_onestop_id = d["operator_onestop_id"])
                route = Route(
                    operator = operator,
                    route_onestop_id = d["route_onestop_id"],
                    name = d["name"],
                    long_name = d["long_name"],
                    vehicle_type = d["vehicle_type"],
                    color = d["color"],
                    geom = MultiLineString(lines)
                )
                route.save()
            except:
                print("Could not add route %s" %d["route_onestop_id"])
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('rom', '0009_route'),
    ]

    operations = [
        migrations.RunPython(load_route_data)
    ]
