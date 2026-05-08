import requests

class Pokemon:
    def __init__(self, data):
        """
        Milestone 2: Data Modeling
        This class takes the 'messy' dictionary from the API and 
        picks out only the parts we care about.
        """
        self.name = data['name'].capitalize()
        self.id = data['id']
        self.height = data['height']
        self.weight = data['weight']
        
        # Extracting types (e.g., ['Electric', 'Flying'])
        self.types = [t['type']['name'].capitalize() for t in data['types']]
        
        # Extracting stats (e.g., {'hp': 35, 'attack': 55})
        self.stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}

    def __str__(self):
        # This makes it easy to print the object later
        return f"Pokemon Object: {self.name} (ID: {self.id})"
    
class Pokedex:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon/"

    def search(self, name_or_id):
        """
        Milestone 3: Search Logic
        Communicates with the API and returns a Pokemon object.
        """
        try:
            # We convert to string and lowercase for the API URL
            response = requests.get(f"{self.base_url}{str(name_or_id).lower()}")
            
            if response.status_code == 200:
                data = response.json()
                return Pokemon(data)
            else:
                return None
        except Exception as e:
            print(f"Connection Error: {e}")
            return None