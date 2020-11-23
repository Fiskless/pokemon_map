from django.db import models


class Pokemon(models.Model):

    title = models.CharField('Имя на русском', max_length=200, blank=True)
    photo = models.ImageField('Фото', upload_to='pokemons', null=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    english_name = models.CharField('Имя на английском', max_length=200, blank=True)
    japanese_name = models.CharField('Имя на японском', max_length=200, blank=True)
    previous_evolution = models.ForeignKey('self',
                                           verbose_name='Из кого эволюционирует',
                                           on_delete=models.SET_NULL,
                                           null=True, blank=True,
                                           related_name='next_evolutions')

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):

    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон',
                                on_delete=models.CASCADE)
    lat = models.FloatField('Ширина', max_length=200)
    lon = models.FloatField('Долгота', max_length=200)
    appeared_at = models.DateTimeField('Появится в')
    disappeared_at = models.DateTimeField('Пропадет в')
    level = models.IntegerField('Уровень', blank=True, null=True)
    health_points = models.IntegerField('Здоровье', blank=True, null=True)
    attack = models.IntegerField('Атака', blank=True, null=True)
    armor = models.IntegerField('Защита', blank=True, null=True)
    endurance = models.IntegerField('Выносливость', blank=True, null=True)

    def __str__(self):
        return f'{self.lat} {self.lon}  {self.pokemon}'
