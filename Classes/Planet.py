from Classes.Film import Film
from Classes.People import People

class Planet:
    name: str  # Nombre del planeta
    orbital_period: int  # Periodo orbital del planeta (días)
    rotation_period: int  # Periodo de rotación del planeta (días)
    population: int  # Población del planeta
    climate: str  # Clima del planeta
    films: list[Film]  # Lista de películas en las que aparece el planeta
    residents: list[People]  # Lista de residentes del planeta

    def __init__(self, name: str, orbital_period: int, rotation_period: int, population: int, 
                 climate: str, films: list[None], residents: list[None]) -> None:
        # Inicializa los atributos del planeta
        self.name = name
        self.orbital_period = orbital_period
        self.rotation_period = rotation_period
        self.population = population
        self.climate = climate
        self.films = films
        self.residents = residents

    def toString(self) -> str:
        # Convierte las listas de films y residents en cadenas separadas por comas
        films: str
        residents: str

        films = ", ".join(film.title for film in self.films)  # Extrae el título de cada film
        residents = ", ".join(resident.name for resident in self.residents)  # Extrae el nombre de cada residente

        # Devuelve una representación en cadena del planeta
        return f"""
        Nombre: {self.name}
        Periodo de orbita: {self.orbital_period}
        Periodo de rotacion: {self.rotation_period}
        Poblacion: {self.population}
        Clima: {self.climate}
        Peliculas: {films}
        Residentes: {residents}
        """
