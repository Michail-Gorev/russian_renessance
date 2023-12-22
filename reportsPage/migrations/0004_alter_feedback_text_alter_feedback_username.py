# Generated by Django 4.2.5 on 2023-12-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsPage', '0003_feedback_text_feedback_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(default='Текст отзыва', max_length=30000, verbose_name='Текст отзыва'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='username',
            field=models.CharField(default='Имя', max_length=255, verbose_name='Имя пользователя'),
        ),
    ]