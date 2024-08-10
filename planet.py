import requests

class Planet:
    planet_list = []

    def __init__(self, name, orbital_period, rotation_period, diameter, climate, gravity, terrain, surface_water, population, residents, films, url, created, edited):
        self.name = name
        self.orbital_period = orbital_period
        self.rotation_period = rotation_period
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.surface_water = surface_water
        self.population = population
        self.residents = residents
        self.films = films
        self.url = url
        self.created = created
        self.edited = edited

def load_names_from_urls(urls):
    names = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        names.append(data['result']['properties']['name'])
    return names

def load_planet_details(url):
    response = requests.get(url)
    data = response.json()['result']['properties']
    residents = load_names_from_urls(data['residents']) if 'residents' in data else []
    films = load_names_from_urls(data['films']) if 'films' in data else []
    planet = Planet(
        name=data['name'],
        orbital_period=data['orbital_period'],
        rotation_period=data['rotation_period'],
        diameter=data['diameter'],
        climate=data['climate'],
        gravity=data['gravity'],
        terrain=data['terrain'],
        surface_water=data['surface_water'],
        population=data['population'],
        residents=residents,
        films=films,
        url=data['url'],
        created=data['created'],
        edited=data['edited']
    )
    Planet.planet_list.append(planet)

def load_planets():
    api_url = "https://www.swapi.tech/api/planets"
    while api_url:
        response = requests.get(api_url)
        data = response.json()
        if 'results' not in data:
            print(f"Error: 'results' key not found in the response: {data}")
            break
        for planet_data in data['results']:
            load_planet_details(planet_data['url'])
        api_url = data.get('next')
