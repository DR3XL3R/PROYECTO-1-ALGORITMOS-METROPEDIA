class Mission():
    name: str
    weapons: list
    members: list

    def __init__(self, name: str, planet, starship, weapons: list, members: list) -> None:
        # Inicializa una misión con nombre, planeta, nave, armas y miembros
        self.name = name
        self.planet = planet
        self.starship = starship
        self.weapons = weapons
        self.members = members

    def toString(self) -> str:
        # Devuelve una cadena que representa la misión, con detalles sobre el nombre, planeta, nave, armas y miembros
        weapons: str = ""
        for idx, i in enumerate(self.weapons):
            if idx == len(self.weapons)-1:
                weapons += i['name']
            
            else:
                weapons += i['name'] + ", "

        members: str = ""
        for idx, i in enumerate(self.members):
            if idx == len(self.members)-1:
                members += i['name']

            else:
                members += i['name'] + ", "

        return f"""
        Nombre: {self.name}
        Planeta: {self.planet['name']}
        Nave: {self.starship['name']}
        Armas: {weapons}
        Miembros: {members}
        """