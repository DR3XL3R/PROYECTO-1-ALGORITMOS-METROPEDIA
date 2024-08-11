class Mision():

    def __init__(self, nombre_mision, planeta_destino, nave, armas, integrantes):
        self.nombre_mision = nombre_mision
        self.planeta_destino = planeta_destino
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes

    def mostrar(self):
        print(f" Nombre De La Mision : {self.nombre_mision}")
        print(f" Planeta Elegido : {self.planeta_destino}")
        print(f" Nave De La Mision: {self.nave}")
        print(f" Armas De La Mision : {self.armas}")
        print(f" Integrantes De La Mision: {self.integrantes}")