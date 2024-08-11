from movie import load_movies, Movie
from planet import load_planets, Planet
from starship import load_starships, Starship
from vehicle import load_vehicles, Vehicle
from species import load_species, Species
from lists import list_movies, list_species, list_planets, search_character
from Mision import Mision 
from Usuario import Usuario 

def load_all_data():
    print("Loading data from SWAPI...")
    load_movies()
    load_planets()
    print(f"Loaded {len(Planet.planet_list)} planets.")
    load_starships()
    print(f"Loaded {len(Starship.starship_list)} starships.")
    load_vehicles()
    print(f"Loaded {len(Vehicle.vehicle_list)} vehicles.")
    load_species()
    print(f"Loaded {len(Species.species_list)} species.")
    print("Data loaded successfully.")

def main():
    while True:
        print("\nWelcome to the Galactic Encyclopedia!")
        print("Ingresa la pocion que deseas:")
        print("1. Mostrar ")
        print("2. Gráficas")
        print("3. Mision ")

        selection = input("===> ")

        if selection == '1':
            print("1. Lista De Peliculas")
            print("2. Lista De Especies")
            print("3. Lista De Planetas")
            sub_selection = input("===> ")

            if sub_selection == '1':
                list_movies()
            elif sub_selection == '2':
                list_species()
            elif sub_selection == '3':
                list_planets()
            else:
                print("Invalid selection.")
        
        elif selection == '2':
            search_character()
        
        elif selection == "3":
            usuario = input("Ingrese Su Usuario: ")
            usuario.lower() 
            usuario_registrado()
        
         #verificando si el usuario ya esta registrado. Si no lo esta, inicia el registro  
def usuario_registrado(usuario):
    usuarios = []
    if usuario not in usuarios: 
        name = input("ingrese su nombre: ")
        apellido = input("ingrese su apellido")
        user = input("Cree su usuario: ")
        if usuarios[user] == user:
            print("El usuario ya existe")
        else:
            usuarios[user] = user
            print(f"Usuario {usuario} registrado!")
                
    else: 
        print(f"Bienvenido {usuario} !")
            
        print("Menú: ")
        print("1. Crear misión")
        print("2. Ver misiones")
        print("3. Modificar misión")
        print("4. Regresar al menu")
        sub_selection = input("===> ")

        if sub_selection =="1":
            crear_mision(usuario)
            
        elif sub_selection =="2":
            pass
        elif sub_selection =="3":
            pass
        elif sub_selection =="4":
            main()
        else:
            print("Invalid selection.")


def crear_mision(usuario):
            print("Ingrese los datos de la misión: ")
            nombre = input("Nombre De la mision: ")
            planeta= input(" Planeta Elegido: ")
            nave = input("Nave De La Mision: ")
            armas= []
            for a in range(7):
                arma = input("armas de la mision: ")
             
            if arma: 
                armas.append(arma)
            else:
                pass 
            integrantes=[]
            for i in range(7):
                integrante = input("Ingresa el Integrante De La Mision: ")
            if integrante:
                integrantes.append(integrante)
            else:
                pass
            misión = Mision(nombre, planeta, nave, armas, integrantes)
            usuario_registrado[usuario].add_mision(misión)
            print("Mision Creada. Que la fuerza te acompañe !!!")
        
            
main()