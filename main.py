from movie import load_movies, Movie
from planet import load_planets, Planet
from starship import load_starships, Starship
from vehicle import load_vehicles, Vehicle
from species import load_species, Species
from lists import list_movies, list_species, list_planets, search_character

def load_all_data():
    print("Loading data from SWAPI...")
    load_movies()
    load_planets()
    print(f"Loaded {len(Planet.planet_list)} planets.")
    load_starships()
    print(f"Loaded {len(Starship.starship_list)} starships.")
    load_vehicles()
    print(f"Loaded {len(Vehicle.vehicle_list)} vehicles.")
    load_species()
    print(f"Loaded {len(Species.species_list)} species.")
    print("Data loaded successfully.")

def main():
    while True:
        print("\nWelcome to the Galactic Encyclopedia!")
        print("Select what you want to do:")
        print("1. Mostrar ")
        print("2. Gráficas")
        print("3. Mision ")

        selection = input("===> ")

        if selection == '1':
            print("1. Lista De Peliculas")
            print("2. Lista De Especies")
            print("3. Lista De Planetas")
            sub_selection = input("===> ")

            if sub_selection == '1':
                list_movies()
            elif sub_selection == '2':
                list_species()
            elif sub_selection == '3':
                list_planets()
            else:
                print("Invalid selection.")
        
        elif selection == '2':
            search_character()
        
        elif selection == '3':
            #crear misiones y usuario 
main()