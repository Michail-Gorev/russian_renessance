# Generated by Django 4.2.5 on 2023-10-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursPage', '0008_tourdetail_tour_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='tour_id',
            field=models.IntegerField(default=0, verbose_name='ID тура'),
        ),
    ]