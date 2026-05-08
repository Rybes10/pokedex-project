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