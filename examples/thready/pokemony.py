import multiprocessing
import timeit

import requests
import os
import threading

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Zapisano: {filename}")
    else:
        print(f"Błąd pobierania: {url}")

def get_pokemon_data():
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"  # Pobierz pierwszych 151 Pokemonów (pierwsza generacja)
    response = requests.get(url)
    threads = []
    if response.status_code == 200:
        data = response.json()
        for pokemon in data['results']:
            name = pokemon['name']
            url = pokemon['url']
            thread = multiprocessing.Process(target=download_pokemon_image, args=(name, url))
            threads.append(thread)
            thread.start()
    else:
        print("Błąd pobierania danych Pokemonów")

    for t in threads:
         t.join()

def download_pokemon_image(name, url):
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        sprite_url = pokemon_data['sprites']['front_default']
        filename = f"{name}.png"
        download_image(sprite_url, filename)
    else:
        print(f"Błąd pobierania danych Pokemona: {name}")

def main():
    if not os.path.exists("pokemon_images"):
        os.makedirs("pokemon_images")
    os.chdir("pokemon_images")
    get_pokemon_data()

if __name__ == "__main__":
    print(timeit.timeit(main,number=1))