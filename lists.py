from movie import Movie
from species import Species
from planet import Planet

def list_movies():
    if not Movie.movie_list:
        print("No movies found.")
        return
    for movie in Movie.movie_list:
        print(f"Title: {movie.title}")
        print(f"Episode Number: {movie.episode_id}")
        print(f"Release Date: {movie.release_date}")
        print(f"Opening Crawl: {movie.opening_crawl}")
        print(f"Director: {movie.director}")
        print("="*40)

def list_species():
    if not Species.species_list:
        print("No species found.")
        return
    for species in Species.species_list:
        print(f"Name: {species.name}")
        print(f"Height: {species.average_height}")
        print(f"Classification: {species.classification}")
        print(f"Homeworld: {species.homeworld}")
        print(f"Language: {species.language}")
        print(f"Characters: {', '.join(species.people)}")
        print(f"Episodes: {', '.join(species.films)}")
        print("="*40)

def list_planets():
    if not Planet.planet_list:
        print("No planets found.")
        return
    for planet in Planet.planet_list:
        print(f"Name: {planet.name}")
        print(f"Orbital Period: {planet.orbital_period}")
        print(f"Rotation Period: {planet.rotation_period}")
        print(f"Population: {planet.population}")
        print(f"Climate: {planet.climate}")
        print(f"Episodes: {', '.join(planet.films)}")
        print(f"Residents: {', '.join(planet.residents)}")
        print("="*40)

def search_character():
    query = input("Enter character name or part of the name: ").strip().lower()
    matches = [char for char in Character.character_list if query in char.name.lower()]
    if matches:
        for character in matches:
            print(f"Name: {character.name}")
            print(f"Homeworld: {character.homeworld}")
            print(f"Episodes: {', '.join(character.films)}")
            print(f"Gender: {character.gender}")
            print(f"Species: {', '.join(character.species)}")
            print(f"Ships: {', '.join(character.starships)}")
            print(f"Vehicles: {', '.join(character.vehicles)}")
            print("="*40)
    else:
        print("No characters found.")
