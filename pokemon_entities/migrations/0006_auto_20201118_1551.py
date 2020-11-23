# Generated by Django 2.2.3 on 2020-11-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_pokemon_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='english_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='japanese_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
