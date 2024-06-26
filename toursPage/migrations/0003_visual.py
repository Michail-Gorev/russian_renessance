# Generated by Django 4.2.5 on 2023-10-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursPage', '0002_tour_duration_tour_is_available_for_children_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=120, verbose_name='Файл картинки')),
                ('title', models.CharField(max_length=120, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Описание')),
                ('alt', models.TextField(verbose_name='Подсказка')),
                ('index', models.IntegerField(verbose_name='Индекс')),
            ],
            options={
                'db_table': 'app_ideator_visuals',
            },
        ),
    ]
