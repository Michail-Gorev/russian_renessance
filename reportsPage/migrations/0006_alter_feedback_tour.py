# Generated by Django 4.2.5 on 2023-12-15 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toursPage', '0010_category_tour_cat'),
        ('reportsPage', '0005_alter_feedback_tour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='tour',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Тур', to='toursPage.tour'),
        ),
    ]