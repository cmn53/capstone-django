# Generated by Django 2.0.7 on 2018-07-15 05:53

import json
from django.db import migrations
from django.contrib.gis.db import models


def load_operator_data(apps, schema_editor):
    Metro = apps.get_model('rom', 'Metro')
    Operator = apps.get_model('rom', 'Operator')

    with open('rom/static/data/operator_data.json') as json_file:
        data = json.load(json_file)

        for d in data:
            try:
                metro = Metro.objects.get(metro_code = d["metro_code"])
                operator = Operator(
                    metro = metro,
                    name = d["name"],
                    operator_onestop_id = d["operator_onestop_id"]
                )
                operator.save()
            except:
                print("Could not add operator %s" %d["name"])
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('rom', '0007_operator'),
    ]

    operations = [
        migrations.RunPython(load_operator_data)
    ]
