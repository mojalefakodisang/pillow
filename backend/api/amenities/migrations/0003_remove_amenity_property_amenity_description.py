# Generated by Django 5.0.6 on 2024-06-14 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenities', '0002_amenity_property'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amenity',
            name='property',
        ),
        migrations.AddField(
            model_name='amenity',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
