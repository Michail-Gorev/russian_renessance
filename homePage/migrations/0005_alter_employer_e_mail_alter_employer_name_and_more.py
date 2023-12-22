# Generated by Django 4.2.5 on 2023-12-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0004_rename_user_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='e_mail',
            field=models.EmailField(max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='employer',
            name='name',
            field=models.CharField(max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='employer',
            name='organization',
            field=models.TextField(max_length=1000, verbose_name=''),
        ),
    ]
