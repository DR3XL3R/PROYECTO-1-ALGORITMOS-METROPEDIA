import requests

class Vehicle:
    vehicle_list = []

    def __init__(self, name, model, manufacturer, cost, length, crew, passengers, max_atmosphering_speed, cargo_capacity, consumables, films, pilots, url, created, edited):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost = cost
        self.length = length
        self.crew = crew
        self.passengers = passengers
        self.max_atmosphering_speed = max_atmosphering_speed
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

def load_vehicle_details(url):
    response = requests.get(url)
    data = response.json()['result']['properties']
    vehicle = Vehicle(
        name=data['name'],
        model=data['model'],
        manufacturer=data['manufacturer'],
        cost=data['cost_in_credits'],
        length=data['length'],
        crew=data['crew'],
        passengers=data['passengers'],
        max_atmosphering_speed=data['max_atmosphering_speed'],
        cargo_capacity=data['cargo_capacity'],
        consumables=data['consumables'],
        films=load_names_from_urls(data['films']),
        pilots=load_names_from_urls(data['pilots']),
        url=data['url'],
        created=data['created'],
        edited=data['edited']
    )
    Vehicle.vehicle_list.append(vehicle)

def load_vehicles():
    api_url = "https://www.swapi.tech/api/vehicles"
    while api_url:
        response = requests.get(api_url)
        data = response.json()
        if 'results' not in data:
            print(f"Error: 'results' key not found in the response: {data}")
            break
        for vehicle_data in data['results']:
            load_vehicle_details(vehicle_data['url'])
        api_url = data.get('next')
