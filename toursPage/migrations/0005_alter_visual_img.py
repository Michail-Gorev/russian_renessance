# Generated by Django 4.2.5 on 2023-10-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursPage', '0004_alter_visual_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visual',
            name='img',
            field=models.ImageField(upload_to='media/images', verbose_name='Файл картинки'),
        ),
    ]
