# Generated by Django 3.1.5 on 2021-01-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_close_treasure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='close_treasure',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]