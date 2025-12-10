class estudiante:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        
mi_estudiante = estudiante("Python Avanzado", "curso basico")

print(mi_estudiante.nombre)
print(mi_estudiante.curso)
