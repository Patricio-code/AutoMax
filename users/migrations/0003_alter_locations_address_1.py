# Generated by Django 5.2.3 on 2025-07-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='address_1',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
