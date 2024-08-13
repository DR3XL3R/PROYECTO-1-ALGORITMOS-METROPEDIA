from Modules.SwapiModule import SwapiModule
from CsvModule import CsvModule
from Modules.MissionsModule import MissionsModule
from util import *

class Menu:

    def __init__(self) -> None:
        # Inicializa los módulos para el menú
        self.MissionsModule: MissionsModule = MissionsModule()
        self.swapi: SwapiModule = SwapiModule()
        self.csv: CsvModule = CsvModule()

    async def runMenu(self) -> None:
        # Ejecuta el menú principal y maneja las opciones del usuario
        run: bool = True

        while(run):
            option: int 
        
            clear()
            print("""
            =========================================
                Bienvenido a Star Wars Metropedia!
            -----------------------------------------
            1. Ver datos de SWAPI
            2. Ver datos de CSV                                                                
            3. Misiones
            4. Salir
                """)
            option = input_options(4)

            if option == 1:
                await self.runSWAPI()
            
            elif option == 2:
                self.runCSV()
            
            elif option == 3:
                self.runMissions()
            
            elif option == 4:
                run = False
    
    async def runSWAPI(self) -> None:        
        # Ejecuta el menú de SWAPI y maneja las opciones del usuario
        await self.swapi.loadFilms()               
        await self.swapi.loadVehiclesAndStarships()               

        run: bool = True

        while(run):
            option: int 
        
            clear()
            print("""
                        Metropedia SWAPI
            -----------------------------------------
            1. Ver peliculas
            2. Ver especies de seres vivos
            3. Ver planetas
            4. Buscar personajes 
            5. Regresar                                                              
                """)
            option = input_options(5)

            clear()
            if option == 1: 
                self.swapi.viewFilms()
            
            elif option == 2:                
                await self.swapi.viewSpecies()

            elif option == 3:
                await self.swapi.viewPlanets()
            
            elif option == 4:                
                await self.swapi.searchPeople()
            
            else:
                run = False

            exit()
    
    def runCSV(self):        
        # Ejecuta el menú de CSV y maneja las opciones del usuario
        run: bool = True

        while(run):
            option: int 
        
            clear()
            print("""
                        Metropedia CSV
            ----------------------------------------------------------------
            1. Gráfico de cantidad de personajes nacidos en cada planeta
            2. Gráficos de características de naves
            3. Estadísticas sobre naves             
            4. Salir                                                              
                """)
            option = input_options(4)

            clear()
            if option == 1: 
                self.csv.option1()
            
            elif option == 2:                
                self.csv.option2()

            elif option == 3:
                self.csv.option3()
            
            elif option == 4:                
                run = False

            exit()        

    def runMissions(self):
        # Ejecuta el menú de misiones y maneja las opciones del usuario
        run: bool = True

        while(run):
            option: int 
        
            clear()
            print("""
                        Missiones
            ------------------------------------
            1. Crear Mision
            2. Modificar Mision
            3. Ver Mision    
            4. Guardar cambios
            5. Cargar datos almacenados       
            6. Regresar                                                              
            """)
            option = input_options(6)

            clear()
            if option == 1: 
                self.MissionsModule.createMission()
            
            elif option == 2:                
                self.MissionsModule.modifyMission()

            elif option == 3:
                self.MissionsModule.viewMission()
            
            elif option == 4:                
                self.MissionsModule.saveChanges()
            
            elif option == 5:
                self.MissionsModule.loadData()
            
            else:
                run = False

            exit()
