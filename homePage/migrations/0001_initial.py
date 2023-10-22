# Generated by Django 4.2.5 on 2023-09-21 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='User name')),
                ('e_mail', models.CharField(max_length=255, verbose_name='e-mail address')),
                ('organization', models.TextField(max_length=1000, verbose_name='Organization')),
                ('request_time', models.DateTimeField(verbose_name='Time of request')),
            ],
        ),
    ]