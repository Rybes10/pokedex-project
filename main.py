import requests

def get_pokemon_data(name):
    """
    Fetches raw JSON data from PokeAPI for a specific pokemon name or ID.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def start_ui():
    """
    The basic UI loop for Milestone 1.
    """
    print("--- Welcome to the Pokedex ---")
    while True:
        search_term = input("\nEnter a Pokemon name to search (or 'quit' to exit): ").strip()
        
        if search_term.lower() == 'quit':
            break
            
        data = get_pokemon_data(search_term)
        
        if data:
            # For Milestone 1, we just need to prove we got the data
            print(f"Successfully found: {data['name'].capitalize()}!")
            print(f"ID: {data['id']}")
            print(f"Base Experience: {data['base_experience']}")
        else:
            print("Pokemon not found. Check your spelling!")

if __name__ == "__main__":
    start_ui()