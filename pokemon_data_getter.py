from bs4 import BeautifulSoup
import requests
from pokemon_parser import parse_pokemon_data
from file_writer import write_to_json


def get_pokemon_data():
    base_url = 'https://scrapeme.live/shop'
    page_number = 1
    id_counter = 1
    decomposed_pokemons = []

    while True:
        url = f'{base_url}/page/{page_number}/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        if soup.findAll('div', class_='error-404 not-found'):
            break
        all_pokemons = soup.findAll('li', class_='type-product')
        for pokemon_item in all_pokemons:
            pokemon_data = parse_pokemon_data(pokemon_item, id_counter)
            decomposed_pokemons.append(pokemon_data)
            id_counter += 1

        page_number += 1

    write_to_json(decomposed_pokemons, 'pokemons.json')
