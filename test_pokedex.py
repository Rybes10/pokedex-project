import unittest
from models import Pokedex, Pokemon

class TestPokedex(unittest.TestCase):
    def setUp(self):
        self.pokedex = Pokedex()

    def test_valid_pokemon_search(self):
        # Test if searching for Pikachu (ID 25) works
        pokemon = self.pokedex.search("pikachu")
        self.assertIsNotNone(pokemon)
        self.assertEqual(pokemon.name, "Pikachu")
        self.assertEqual(pokemon.id, 25)

    def test_invalid_pokemon_search(self):
        # Test if searching for a fake name returns None
        pokemon = self.pokedex.search("not_a_real_pokemon")
        self.assertIsNone(pokemon)

    def test_pokemon_class_data(self):
        # Test if our class correctly handles types
        pokemon = self.pokedex.search(1) # Bulbasaur
        self.assertIn("Grass", pokemon.types)

if __name__ == "__main__":
    unittest.main()