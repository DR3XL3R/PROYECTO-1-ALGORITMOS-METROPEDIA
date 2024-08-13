from datetime import date

class Film:
    title: str  # Título de la película
    episode_id: int  # Número de episodio de la película
    release_date: date  # Fecha de lanzamiento de la película
    opening_crawl: str  # Texto de apertura de la película
    director: str  # Director de la película
    characters: list[int]  # Lista de IDs de personajes en la película
    planets: list[int]  # Lista de IDs de planetas en la película
    starships: list[int]  # Lista de IDs de naves estelares en la película
    vehicles: list[int]  # Lista de IDs de vehículos en la película
    species: list[int]  # Lista de IDs de especies en la película

    def __init__(self, title: str, episode_id: int, release_date: date, opening_crawl: str, director: str,
                 characters: list[int], planets: list[int], starships: list[int], vehicles: list[int], species: list[int]) -> None:
        # Inicializa los atributos de la película
        self.title = title
        self.episode_id = episode_id
        self.release_date = release_date
        self.opening_crawl = opening_crawl
        self.director = director
        self.characters = characters
        self.planets = planets
        self.starships = starships
        self.vehicles = vehicles
        self.species = species

    def toString(self) -> str:
        # Devuelve una representación en cadena de la película
        return f"""
----------------------------------------
Titulo: {self.title}
Numero de capitulo: {self.episode_id}
Fecha de lanzamiento: {self.release_date}
Director: {self.director}

Apertura:

{self.opening_crawl}
----------------------------------------
    """
