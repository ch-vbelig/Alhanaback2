# Generated by Django 4.1.13 on 2024-05-19 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_remove_location_vr_image'),
        ('vrphoto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vrphoto',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vrphoto', to='location.location'),
        ),
    ]
