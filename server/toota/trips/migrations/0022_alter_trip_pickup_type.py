# Generated by Django 5.0.2 on 2024-02-21 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0021_alter_trip_created_alter_trip_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='pickup_type',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]