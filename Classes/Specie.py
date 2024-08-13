from Classes.People import People
from Classes.Film import Film

class Specie:
    name: str  # Nombre de la especie
    average_height: int  # Altura promedio de la especie
    classification: str  # Clasificación de la especie (e.g., mamífero, reptil)
    homeworld: str  # Planeta de origen de la especie
    language: str  # Lengua materna de la especie
    people: list[str]  # Lista de personajes de la especie
    films: list[str]  # Lista de películas en las que aparece la especie

    def __init__(self, name: str, average_height: float, classification: str, homeworld: str, 
                 language: str, people: list[str], films: list[str]) -> None:
        # Inicializa los atributos de la especie
        self.name = name
        self.average_height = average_height
        self.classification = classification
        self.homeworld = homeworld
        self.language = language
        self.people = people
        self.films = films

    def toString(self) -> str:
        # Convierte las listas de people y films en cadenas separadas por comas
        people: str
        films: str

        people = ", ".join(self.people)  # Lista de nombres de personajes
        films = ", ".join(self.films)  # Lista de títulos de películas

        # Devuelve una representación en cadena de la especie
        return f"""
        Nombre: {self.name}
        Altura: {self.average_height}
        Clasificacion: {self.classification}
        Planeta de origen: {self.homeworld}
        Lengua materna: {self.language}
        Personajes: {people}
        Capitulos: {films}
        """
