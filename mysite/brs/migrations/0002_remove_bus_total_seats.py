# Generated by Django 3.0.14 on 2022-01-15 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='total_seats',
        ),
    ]