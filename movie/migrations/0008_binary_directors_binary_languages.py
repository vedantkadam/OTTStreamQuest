# Generated by Django 4.0.1 on 2022-03-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_remove_movie_production_companies_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='binary',
            name='directors',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='binary',
            name='languages',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]