# Generated by Django 4.0.3 on 2023-02-12 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='descr',
            field=models.TextField(default='enter'),
            preserve_default=False,
        ),
    ]
