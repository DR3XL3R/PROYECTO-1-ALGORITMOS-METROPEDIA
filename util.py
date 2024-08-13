import requests
import aiohttp
import asyncio
from os import system
import csv
import pickle



def getCSV(path) -> list:
    # Lee un archivo CSV y devuelve el contenido como una lista de diccionarios
    elements = []
    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            elements.append(row)
    return elements

def input_int(str) -> int:
    # Solicita al usuario un número entero y lo devuelve, asegurando que la entrada sea válida
    value = input(str)
    while not value.isnumeric():
        value = input(f"Error: {str}")
    return int(value)

def input_str(str) -> str:
    # Solicita al usuario una cadena de texto y la devuelve, asegurando que la entrada no sea un número
    value = input(str)
    while value.isnumeric():
        value = input(f"Error: {str}")
    return value

def input_options(options) -> int:
    # Solicita al usuario una opción de un rango específico y la devuelve, asegurando que la entrada sea válida
    value = input("Ingrese el numero de la opcion deseada\n>> ")
    while not value.isnumeric() or int(value) not in range(1, int(options)+1):
        value = input("Error: ingrese el numero de la opcion deseada\n>> ")
    return int(value)

def clear() -> None:
    # Limpia la pantalla de la consola
    system('cls')

def exit() -> None:
    # Pausa la ejecución hasta que el usuario presione Enter
    input("Presione enter para salir...")

def saveTXT(route, data) -> None:
    # Guarda datos en un archivo utilizando pickle
    with open(route, 'wb') as archivo:
        pickle.dump(data, archivo)

def readTXT(route) -> object:
    # Lee datos desde un archivo utilizando pickle y los devuelve
    with open(route, 'rb') as archivo:    
        data = pickle.load(archivo)
        return data
