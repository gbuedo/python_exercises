# ejercicio 16

class estudiante:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
    def saludar(self):
        print(f'Hola, soy {self.nombre} y estoy inscrito en el {self.curso}')
                
mi_estudiante = estudiante("Python Avanzado", "curso basico")

mi_estudiante.saludar()

print(mi_estudiante.nombre)
print(mi_estudiante.curso)
