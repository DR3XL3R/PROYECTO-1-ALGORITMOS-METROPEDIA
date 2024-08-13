class Vehicle:
    name: str  # Nombre del vehículo
    pilots: list[int]  # Lista de IDs de los pilotos del vehículo

    def __init__(self, name, pilots) -> None:
        # Inicializa los atributos del vehículo
        self.name = name
        self.pilots = pilots
    
    def toString(self) -> str:
        # Devuelve una representación en cadena del vehículo
        return f"""
        Nombre: {self.name}
        Pilotos: {self.pilots}
        """
