# Generated by Django 4.2.5 on 2023-12-22 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reportsPage', '0008_alter_feedback_tour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='username',
            field=models.ForeignKey(default='Имя', max_length=255, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]