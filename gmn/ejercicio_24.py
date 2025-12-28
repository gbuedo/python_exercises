# ejercicio 16

class estudiante:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
    def saludar(self):
        print(f'Hola, soy {self.nombre} y estoy inscrito en el {self.curso}')
    @classmethod
    def crear_desde_lista(cls, datos_lista):
        nombre, curso = datos_lista
        return cls(datos_lista[0], datos_lista[1])
    
estudiante_por_lista = estudiante.crear_desde_lista(["Luisa", "Base de datos"])

print(estudiante_por_lista.nombre)
    

