import requests

class Starship:
    starship_list = []

    def __init__(self, name, model, manufacturer, cost, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, mglt, cargo_capacity, consumables, films, pilots, url, created, edited):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost = cost
        self.length = length
        self.crew = crew
        self.passengers = passengers
        self.max_atmosphering_speed = max_atmosphering_speed
        self.hyperdrive_rating = hyperdrive_rating
        self.mglt = mglt
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.films = films
        self.pilots = pilots
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

def load_starship_details(url):
    response = requests.get(url)
    data = response.json()['result']['properties']
    films = load_names_from_urls(data['films']) if 'films' in data else []
    pilots = load_names_from_urls(data['pilots']) if 'pilots' in data else []
    starship = Starship(
        name=data['name'],
        model=data['model'],
        manufacturer=data['manufacturer'],
        cost=data['cost_in_credits'],
        length=data['length'],
        crew=data['crew'],
        passengers=data['passengers'],
        max_atmosphering_speed=data['max_atmosphering_speed'],
        hyperdrive_rating=data['hyperdrive_rating'],
        mglt=data['MGLT'],
        cargo_capacity=data['cargo_capacity'],
        consumables=data['consumables'],
        films=films,
        pilots=pilots,
        url=data['url'],
        created=data['created'],
        edited=data['edited']
    )
    Starship.starship_list.append(starship)

def load_starships():
    api_url = "https://www.swapi.tech/api/starships"
    while api_url:
        response = requests.get(api_url)
        data = response.json()
        if 'results' not in data:
            print(f"Error: 'results' key not found in the response: {data}")
            break
        for starship_data in data['results']:
            load_starship_details(starship_data['url'])
        api_url = data.get('next')
