# Generated by Django 2.2.3 on 2020-11-17 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20201117_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(null=True, upload_to='pokemons'),
        ),
    ]