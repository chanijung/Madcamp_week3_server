# Generated by Django 3.1.5 on 2021-01-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='seeker',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='treasure',
            name='timeSought',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]