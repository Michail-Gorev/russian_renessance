# Generated by Django 4.2.5 on 2023-12-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationPage', '0004_customer_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='', max_length=255),
        ),
    ]
