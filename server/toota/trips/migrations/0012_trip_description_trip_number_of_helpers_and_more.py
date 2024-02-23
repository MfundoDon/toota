# Generated by Django 5.0.2 on 2024-02-21 07:44

from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0011_trip_bid_trip_is_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='description',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='number_of_helpers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trip',
            name='pickup_type',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='trip',
            name='dropoff_location',
            field=models.ManyToManyField(blank=True, related_name='dropoff_location', to='trips.pickuplocation'),
        ),
    ]