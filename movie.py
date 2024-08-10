import requests

class Movie:
    movie_list = []

    def __init__(self, title, episode_id, opening_crawl, director, producer, release_date, species, starships, vehicles, characters, planets, url, created, edited):
        self.title = title
        self.episode_id = episode_id
        self.opening_crawl = opening_crawl
        self.director = director
        self.producer = producer
        self.release_date = release_date
        self.species = species
        self.starships = starships
        self.vehicles = vehicles
        self.characters = characters
        self.planets = planets
        self.url = url
        self.created = created
        self.edited = edited

def load_entity_names(urls):
    names = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        names.append(data['result']['properties']['name'])
    return names

def load_movies():
    api_url = "https://www.swapi.tech/api/films"
    response = requests.get(api_url)
    data = response.json()
    for film_data in data['result']:
        details = film_data['properties']
        movie = Movie(
            title=details['title'],
            episode_id=details['episode_id'],
            opening_crawl=details['opening_crawl'],
            director=details['director'],
            producer=details['producer'],
            release_date=details['release_date'],
            species=load_entity_names(details['species']),
            starships=load_entity_names(details['starships']),
            vehicles=load_entity_names(details['vehicles']),
            characters=load_entity_names(details['characters']),
            planets=load_entity_names(details['planets']),
            url=details['url'],
            created=details['created'],
            edited=details['edited']
        )
        Movie.movie_list.append(movie)
