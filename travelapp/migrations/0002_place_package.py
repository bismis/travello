# Generated by Django 4.0.3 on 2023-02-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='package',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
