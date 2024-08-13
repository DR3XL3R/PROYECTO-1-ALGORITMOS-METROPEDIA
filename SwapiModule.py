from Film import Film
from Specie import Specie
from People import People
from Planet import Planet
from Vehicle import Vehicle
from Starship import Starship
from util import *

class SwapiModule:
    films: list[Film]  # Lista para almacenar objetos Film
    vehicles: list[Vehicle]  # Lista para almacenar objetos Vehicle
    starships: list[Starship]  # Lista para almacenar objetos Starship

    def __init__(self) -> None:
        self.films = []  # Inicializa la lista de films
        self.vehicles = []  # Inicializa la lista de vehicles
        self.starships = []  # Inicializa la lista de starships

    async def loadVehiclesAndStarships(self):
        # Carga los vehículos y naves estelares desde la API
        url = "https://swapi.dev/api/vehicles/"
        vehicleUrls = await getAPI(url)
        for vehicleUrl in vehicleUrls['results']:
            pilots: list[int] = []
            responseVehicle = await getAPI(vehicleUrl['url'])
            for pilotUrl in responseVehicle['pilots']:
                pilots.append(pilotUrl.split("/")[-1])
            self.vehicles.append(Vehicle(
                responseVehicle['name'],
                pilots
            ))

        url = "https://swapi.dev/api/starships/"
        starshipsUrls = await getAPI(url)
        for starshipUrl in starshipsUrls['results']:
            pilots: list[int] = []
            responseStarship = await getAPI(starshipUrl['url'])
            for pilotUrl in responseStarship['pilots']:
                pilots.append(pilotUrl.split("/")[-1])
            self.vehicles.append(Starship(
                responseStarship['name'],
                pilots
            ))

    async def loadFilms(self) -> None:
        # Carga las películas desde la API
        filmsResponse = await getAPI("https://www.swapi.tech/api/films")
        for film in filmsResponse['result']:
            characters: list[int] = []
            planets: list[int] = []
            starships: list[int] = []
            vehicles: list[int] = []
            species: list[int] = []

            for character in film['properties']['characters']:
                characters.append(int(character.split('/')[-1]))
            
            for planet in film['properties']['planets']:
                planets.append(int(planet.split('/')[-1]))

            for starship in film['properties']['starships']:
                starships.append(int(starship.split('/')[-1]))

            for vehicle in film['properties']['vehicles']:
                vehicles.append(int(vehicle.split('/')[-1]))

            for specie in film['properties']['species']:
                species.append(int(specie.split('/')[-1]))

            self.films.append(Film(
                film['properties']['title'],
                film['properties']['episode_id'],
                film['properties']['release_date'],
                film['properties']['opening_crawl'],
                film['properties']['director'],
                characters,
                planets,
                starships,
                vehicles,
                species
            ))

    def viewFilms(self) -> None:
        # Muestra la lista de películas
        for idx, film in enumerate(self.films):
            print(f"{idx+1}. {film.toString()}")

    async def viewSpecies(self) -> None:
        # Muestra la lista de especies
        spieciesUrls = await getAPI('https://www.swapi.tech/api/species')
        for idx, specieUrl in enumerate(spieciesUrls['results']):
            people: list[str] = []
            films: list[str] = []
            
            specieResponse = await getAPI(specieUrl['url'])
            for peopleUrl in specieResponse['result']['properties']['people']:
                peopleResponse = await getAPI(peopleUrl)
                people.append(peopleResponse['result']['properties']['name'])
            
            for film in self.films:
                if int(specieResponse['result']['uid']) in film.species:
                    films.append(film.title)

            specie: Specie = Specie(
                specieResponse['result']['properties']['name'],
                specieResponse['result']['properties']['average_height'],
                specieResponse['result']['properties']['classification'],
                specieResponse['result']['properties']['homeworld'],
                specieResponse['result']['properties']['language'],
                people,
                films
            )

            print(f"{idx+1}. {specie.toString()}")

    async def viewPlanets(self):
        # Muestra la lista de planetas
        planetsUrls = await getAPI('https://www.swapi.tech/api/planets')
        for idx, planetUrl in enumerate(planetsUrls['results']):
            people: list[str] = []
            films: list[str] = []
            
            planetResponse = await getAPI(planetUrl['url'])
            for film in self.films:
                if int(planetResponse['result']['uid']) in film.planets:
                    films.append(film.title)
            
            peopleUrls = await getAPI('https://www.swapi.tech/api/people')
            for peopleUrl in peopleUrls['results']:
                peopleResponse = await getAPI(peopleUrl['url'])
                if planetResponse['result']['properties']['url'] == peopleResponse['result']['properties']['homeworld']:
                    people.append(peopleResponse['result']['properties']['name'])
            
            planet: Planet = Planet(
                planetResponse['result']['properties']['name'],
                planetResponse['result']['properties']['orbital_period'],
                planetResponse['result']['properties']['rotation_period'],
                planetResponse['result']['properties']['population'],
                planetResponse['result']['properties']['climate'],
                films,
                people
            )

            print(f"{idx+1}. {planet.toString()}")

    async def searchPeople(self):
        # Busca personas por nombre e imprime su información
        name: str = input_str("Ingrese el nombre del personaje que desea buscar\n>> ")
        
        peopleUrls = await getAPI('https://www.swapi.tech/api/people')
        for peopleUrl in peopleUrls['results']:
            peopleResponse = await getAPI(peopleUrl['url'])

            if name in peopleResponse['result']['properties']['name']:
                vehicles: list[str] = []
                starships: list[str] = []
                films: list[str] = []

                for vehicleaux in self.vehicles:
                    if int(peopleResponse['result']['uid']) in vehicleaux.pilots:
                        vehicles.append(vehicleaux)

                for starshipaux in self.starships:
                    if int(peopleResponse['result']['uid']) in starshipaux.pilots:
                        starships.append(starshipaux)
                
                for filmAux in self.films:
                    if int(peopleResponse['result']['uid']) in filmAux.characters:
                        films.append(filmAux.title)

                homeworldResponse = await getAPI(peopleResponse['result']['properties']['homeworld'])

                people: People = People(
                    peopleResponse['result']['properties']['name'],
                    homeworldResponse['result']['properties']['name'],
                    films,
                    peopleResponse['result']['properties']['gender'],
                    starships,
                    vehicles
                )

                print(f"{people.toString()}")


#todo luis 