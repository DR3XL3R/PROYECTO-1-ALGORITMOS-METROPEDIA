from util import *
from Classes.Mission import Mission
import pickle

class MissionsModule:

    def __init__(self) -> None:
        # Inicializa la lista de misiones
        self.missions = [] 

    def createMission(self) -> None:
        # Crea una nueva misión y la agrega a la lista de misiones
        if len(self.missions) >= 5:
            print("No puedes crear mas de 5 misiones")
        else:
            clear()
            mision_name: str = input_str("Ingrese nombre de la mision: ")

            clear()
            planets: list = getCSV('Modules\csv\planets.csv')
            for idx, planet in enumerate(planets):
                print(f"{idx+1}. {planet["name"]}")

            print("Destino de la mision")
            planet_idx: int = input_options(len(planets))
            mission_planet = planets[planet_idx-1]
            
            clear()
            starships: list = getCSV('Modules\csv\starships.csv')
            for idx, starship in enumerate(starships):
                print(f"{idx+1}. {starship["name"]}")

            print("Nave de la mision")
            starship_idx: int = input_options(len(starships))
            mission_starship = starships[starship_idx - 1]

            mission_weapons: list = []
            weaponsList: list = getCSV("Modules\\csv\\weapons.csv")

            run = True
            while(run and (len(mission_weapons) < 7)):
                clear()
                for idx, weapon in enumerate(weaponsList):
                    print(f"{idx+1}. {weapon['name']}")
                
                print(f"Seleccione las armas de la mision\nlimite: {7 - len(mission_weapons)}")
                weapon_idx: int = input_options(len(weaponsList))
                mission_weapon = weaponsList[weapon_idx - 1]
                mission_weapons.append(mission_weapon)

                print("Desea agregar otra arma?\n1.Si\n2.No")
                option = input_options(2)
                if option == 2:
                    run = False
            

            mission_members: list = []
            membersList: list = getCSV("Modules\\csv\\characters.csv")

            run = True
            while(run and (len(mission_members) < 7)):
                clear()
                for idx, member in enumerate(membersList):
                    print(f"{idx+1}. {member['name']}")
                
                print(f"Seleccione los integrantes de la mision\nlimite: {7 - len(mission_members)}")
                member_idx: int = input_options(len(membersList))
                mission_member = membersList[member_idx - 1]
                mission_members.append(mission_member)

                print("Desea agregar otro integrante?\n1.Si\n2.No")
                option = input_options(2)
                if option == 2:
                    run = False
            
            mission: Mission = Mission(
                mision_name,
                mission_planet,
                mission_starship,
                mission_weapons,
                mission_members
            )

            self.missions.append(mission)
            print("Mision creada!")

    def modifyMission(self) -> None:
        # Modifica una misión existente
        for idx, mission in enumerate(self.missions):
            print(f"{idx+1}. {mission.name}")
        
        mission_idx = input_options(len(self.missions))
        mission = self.missions[mission_idx - 1]

        print("""
        --------Modificar Mision------
        1. Nombre
        2. Planeta
        3. Nave
        4. Armas
        5. Miembros
        ------------------------------
        """)
        option = input_options(5)

        if option == 1:
            # Cambia el nombre de la misión
            mission.name = input("Ingrese el nuevo nombre de la mision: ")
        
        elif option == 2:
            # Cambia el planeta de la misión
            planets: list = getCSV('Modules\csv\planets.csv')
            for idx, planet in enumerate(planets):
                print(f"{idx+1}. {planet["name"]}")

            print("Destino de la mision")
            planet_idx: int = input_options(len(planets))
            mission_planet = planets[planet_idx - 1]

            mission.planet = mission_planet
        
        elif option == 3:
            # Cambia la nave de la misión
            starships: list = getCSV('Modules\csv\starships.csv')
            for idx, starship in enumerate(starships):
                print(f"{idx+1}. {starship["name"]}")

            print("Nave de la mision")
            starship_idx: int = input_options(len(starships))
            mission_starship = starships[starship_idx - 1]

            mission.starship = mission_starship
        
        elif option == 4:
            # Añade o elimina armas de la misión
            print("""
            1.Agregar Arma
            2.Eliminar Arma
            """)
            option = input_options(2)

            if option == 1:
                # Añade armas a la misión
                if len(mission.weapons) >= 7:
                    print("No se pueden agregar mas armas a la mision")

                else:
                    weaponsList: list = getCSV("Modules\\csv\\weapons.csv")

                    run = True
                    while(run and (len(mission.weapons) < 7)):
                        clear()
                        for idx, weapon in enumerate(weaponsList):
                            print(f"{idx+1}. {weapon['name']}")
                        
                        print(f"Seleccione las armas de la mision\nlimite: {7 - len(mission.weapons)}")
                        weapon_idx: int = input_options(len(weaponsList))
                        mission_weapon = weaponsList[weapon_idx - 1]
                        mission.weapons.append(mission_weapon)

                        print("Desea agregar otra arma?\n1.Si\n2.No")
                        option = input_options(2)
                        if option == 2:
                            run = False
            
            elif option == 2:
                # Elimina armas de la misión
                if len(mission.weapons) < 0:
                    print("No hay armas para eliminar")

                else:                    

                    run = True
                    while(run and (len(mission.weapons) > 0)):
                        clear()
                        for idx, weapon in enumerate(mission.weapons):
                            print(f"{idx+1}. {weapon['name']}")
                        
                        print(f"Seleccione la arma a eliminar de la mision")
                        weapon_idx: int = input_options(len(mission.weapons))                        
                        mission.weapons.pop(weapon_idx - 1)

                        print("Desea eliminar otra arma?\n1.Si\n2.No")
                        option = input_options(2)
                        if option == 2:
                            run = False

        elif option == 5:
            # Añade o elimina miembros de la misión
            print("""
            1.Agregar Miebro
            2.Eliminar Miembro
            """)
            option = input_options(2)

            if option == 1:
                # Añade miembros a la misión
                if len(mission.members) >= 7:
                    print("No se pueden agregar mas miembros a la mision")

                else:
                    membersList: list = getCSV("Modules\\csv\\characters.csv")

                    run = True
                    while(run and (len(mission.members) < 7)):
                        clear()
                        for idx, member in enumerate(membersList):
                            print(f"{idx+1}. {member['name']}")
                        
                        print(f"Seleccione los miembros de la mision\nlimite: {7 - len(mission.members)}")
                        member_idx: int = input_options(len(membersList))
                        mission_member = membersList[member_idx - 1]
                        mission.members.append(mission_member)

                        print("Desea agregar otra miembro?\n1.Si\n2.No")
                        option = input_options(2)
                        if option == 2:
                            run = False
            
            elif option == 2:
                # Elimina miembros de la misión
                if len(mission.members) < 0:
                    print("No hay miembros para eliminar")

                else:                    

                    run = True
                    while(run and (len(mission.members) > 0)):
                        clear()
                        for idx, member in enumerate(mission.members):
                            print(f"{idx+1}. {member['name']}")
                        
                        print(f"Seleccione el miembro a eliminar de la mision")
                        member_idx: int = input_options(len(mission.members))                        
                        mission.members.pop(member_idx - 1)

                        print("Desea eliminar otra miembro?\n1.Si\n2.No")
                        option = input_options(2)
                        if option == 2:
                            run = False

    def viewMission(self) -> None:
        # Muestra una lista de misiones y permite ver los detalles de una misión seleccionada
        if len(self.missions) <= 0:
            print("No hay misiones")

        else:
            for idx, mission in enumerate(self.missions):
                print(f"{idx+1}. {mission.name}")
            
            mission_idx = input_options(len(self.missions))
            mission = self.missions[mission_idx - 1]

            print(mission.toString())
    
    def saveChanges(self) -> None:
        # Guarda la lista de misiones en un archivo
        saveTXT("Modules\\missions.txt", self.missions)
        print("Cambios guardados!")
    
    def loadData(self) -> None:
        # Carga la lista de misiones desde un archivo
        self.missions = readTXT("Modules\\missions.txt")
        print("Datos cargados!")
