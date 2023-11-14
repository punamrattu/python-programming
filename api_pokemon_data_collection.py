"""
The code uses the Pokémon API to fetch data for a list of 6 Pokémon IDs. For each ID, it retrieves the Pokémon's information including name, height, and weight, and writes this data to a file named 'pokemon.txt'.
"""


import requests

def write_data(id):
    """
    Fetches data for a Pokémon ID from the Pokémon API and writes it to a file.

    Args:
        id (int): The ID of the Pokémon to fetch and write to file.
    """
    # Form the URL for the Pokémon ID
    url = f'https://pokeapi.co/api/v2/pokemon/{id}/'

    # Request data from the API
    response = requests.get(url)
    pokemon = response.json()

    # Extract required data and format it for writing
    file_text = f"{pokemon['name']} {pokemon['height']} {pokemon['weight']}\n"

    # Append data to a file named 'pokemon.txt'
    with open('pokemon.txt', 'a') as file:
        file.write(file_text)

# Fetch and write data for Pokémon IDs from 1 to 5
for i in range(1, 6):
    write_data(i)
