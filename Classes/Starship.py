class Starship:
    name: str  # Nombre de la nave estelar
    pilots: list[int]  # Lista de IDs de los pilotos de la nave

    def __init__(self, name, pilots) -> None:
        # Inicializa los atributos de la nave estelar
        self.name = name
        self.pilots = pilots
    
    def toString(self) -> str:
        # Devuelve una representación en cadena de la nave estelar
        return f"""
        Nombre: {self.name}
        Pilotos: {self.pilots}
        """
