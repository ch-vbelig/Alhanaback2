# Generated by Django 4.1.13 on 2024-05-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='vr_image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]