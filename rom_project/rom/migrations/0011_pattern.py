# Generated by Django 2.0.7 on 2018-07-15 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rom', '0010_auto_20180715_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern_onestop_id', models.CharField(max_length=100)),
                ('wk_trips', models.IntegerField()),
                ('sa_trips', models.IntegerField()),
                ('su_trips', models.IntegerField()),
                ('wk_00_03', models.IntegerField()),
                ('wk_03_06', models.IntegerField()),
                ('wk_06_09', models.IntegerField()),
                ('wk_09_12', models.IntegerField()),
                ('wk_12_15', models.IntegerField()),
                ('wk_15_18', models.IntegerField()),
                ('wk_18_21', models.IntegerField()),
                ('wk_21_24', models.IntegerField()),
                ('wk_24_28', models.IntegerField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rom.Route')),
            ],
        ),
    ]
