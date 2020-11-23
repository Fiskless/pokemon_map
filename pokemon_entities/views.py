import folium

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render
from pokemon_entities.models import Pokemon
from pokemon_entities.models import PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6" \
                    "/6e/%21.png/revision/latest/fixed-aspect-ratio-down" \
                    "/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):

    pokemons_entity = PokemonEntity.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entity:
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon_entity.pokemon.title, request.build_absolute_uri(
                pokemon_entity.pokemon.photo.url)
        )


    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.photo.url,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    try:
        requested_pokemon = Pokemon.objects.get(id=pokemon_id)

    except:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    try:
        previous_evolution = {
            "title_ru": requested_pokemon.previous_evolution.title,
            "pokemon_id": requested_pokemon.previous_evolution.id,
            "img_url": requested_pokemon.previous_evolution.photo.url
        }
    except AttributeError:
        previous_evolution = {
            "title_ru": "Doesn't evolve",
            "pokemon_id": None,
            "img_url": DEFAULT_IMAGE_URL
        }

    try:
        next_evolution = {
            "title_ru": requested_pokemon.next_evolutions.get().title,
            "pokemon_id": requested_pokemon.next_evolutions.get().id,
            "img_url": requested_pokemon.next_evolutions.get().photo.url
        }
    except ObjectDoesNotExist:
        next_evolution = {
            "title_ru": "Doesn't evolve",
            "pokemon_id": None,
            "img_url": DEFAULT_IMAGE_URL
        }

    pokemon = {
            "title_ru": requested_pokemon.title,
            "title_en": requested_pokemon.english_name,
            "title_jp": requested_pokemon.japanese_name,
            "description": requested_pokemon.description,
            "img_url": request.build_absolute_uri(requested_pokemon.photo.url),
            "previous_evolution": previous_evolution,
            "next_evolution": next_evolution
             }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_entity = PokemonEntity.objects.filter(pokemon__id=pokemon_id)

    for pokemon_entity in pokemons_entity:

        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon_entity.pokemon.title,
            request.build_absolute_uri(pokemon_entity.pokemon.photo.url))

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})

