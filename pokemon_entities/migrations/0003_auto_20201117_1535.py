# Generated by Django 2.2.3 on 2020-11-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20201117_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='armor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='attack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='endurance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
