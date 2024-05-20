# Generated by Django 5.0.2 on 2024-04-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_driverprofile_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/profile_pictures'),
        ),
        migrations.DeleteModel(
            name='DriverProfile',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]