# Generated by Django 4.0.4 on 2022-12-07 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
