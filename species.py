import requests

class Species:
    species_list = []

    def __init__(self, name, classification, designation, average_height, average_lifespan, hair_colors, skin_colors, eye_colors, homeworld, language, people, films, url, created, edited):
        self.name = name
        self.classification = classification
        self.designation = designation
        self.average_height = average_height
        self.average_lifespan = average_lifespan
        self.hair_colors = hair_colors
        self.skin_colors = skin_colors
        self.eye_colors = eye_colors
        self.homeworld = homeworld
        self.language = language
        self.people = people
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

def load_species_details(url):
    response = requests.get(url)
    data = response.json()['result']['properties']
    films = load_names_from_urls(data['films']) if 'films' in data else []
    people = load_names_from_urls(data['people']) if 'people' in data else []
    species = Species(
        name=data['name'],
        classification=data['classification'],
        designation=data['designation'],
        average_height=data['average_height'],
        average_lifespan=data['average_lifespan'],
        hair_colors=data['hair_colors'],
        skin_colors=data['skin_colors'],
        eye_colors=data['eye_colors'],
        homeworld=load_homeworld_name(data['homeworld']),
        language=data['language'],
        people=people,
        films=films,
        url=data['url'],
        created=data['created'],
        edited=data['edited']
    )
    Species.species_list.append(species)

def load_homeworld_name(url):
    response = requests.get(url)
    data = response.json()
    return data['result']['properties']['name']

def load_species():
    api_url = "https://www.swapi.tech/api/species"
    while api_url:
        response = requests.get(api_url)
        data = response.json()
        if 'results' not in data:
            print(f"Error: 'results' key not found in the response: {data}")
            break
        for species_data in data['results']:
            load_species_details(species_data['url'])
        api_url = data.get('next')
