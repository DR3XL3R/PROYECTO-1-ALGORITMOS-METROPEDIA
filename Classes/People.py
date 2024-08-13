class People:
    name: str  # Nombre de la persona
    homeworld: str  # Planeta de origen de la persona
    films: list[str]  # Lista de películas en las que aparece la persona
    gender: str  # Género de la persona
    starships: list[str]  # Lista de naves estelares que la persona ha pilotado
    vehicles: list[str]  # Lista de vehículos que la persona ha utilizado

    def __init__(self, name: str, homeworld: str, films: list[str], gender: str, 
                 starships: list[str], vehicles: list[str]) -> None:
        # Inicializa los atributos de la persona
        self.name = name
        self.homeworld = homeworld
        self.films = films
        self.gender = gender        
        self.starships = starships
        self.vehicles = vehicles

    def toString(self) -> str:
        # Convierte las listas de films, starships y vehicles en cadenas separadas por comas
        films: str = ""       
        starships: str = ""
        vehicles: str = ""

        if len(self.films) > 0:
            films = ", ".join(self.films) 

        if len(self.starships) > 0:
            starships = ", ".join(self.starships)

        if len(self.vehicles) > 0:
            vehicles = ", ".join(self.vehicles)

        # Devuelve una representación en cadena de la persona
        return f"""
        Nombre: {self.name}
        Planeta de origen: {self.homeworld}
        Peliculas: {films}
        Genero: {self.gender}        
        Naves: {starships}
        Vehiculos: {vehicles}
        """
