from Mision import Mision 

class Usuario:
    def __init__(self, nombre, apellido, usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.misiones = []

    #Crear misiones y añadirla al usuario 
    def misiones_añadir (self, mision):
        self.misiones.append(mision)

    def mostrar(self):
        print(f"Usuario: {self.usuario}")
        print(f"Misiones: {self.misiones}")
