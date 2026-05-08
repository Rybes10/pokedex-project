from models import Pokedex

def main():
    # Initialize our manager class
    pokedex_manager = Pokedex()
    
    print("Welcome to your Python Pokedex!")
    
    while True:
        choice = input("\nEnter Pokemon Name/ID (or 'q' to quit): ").strip()
        
        if choice.lower() == 'q':
            break
            
        # Use the Pokedex class to find the pokemon
        result = pokedex_manager.search(choice)
        
        if result:
            print(f"\n--- {result} ---")
            print(f"Height: {result.height} | Weight: {result.weight}")
            print("Base Stats:")
            for stat, value in result.stats.items():
                print(f"  * {stat.capitalize()}: {value}")
        else:
            print(f"\n[!] Pokemon '{choice}' not found. Try 'Pikachu' or '25'.")

if __name__ == "__main__":
    main()