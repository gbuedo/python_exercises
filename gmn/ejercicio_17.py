# ejercicio 17.py

import pandas as pd

usuarios = [
{"nombre": "Maria", "edad": 30, "salario": 10300},
{"nombre": "Pedro", "edad": 25, "salario": 15100},
{"nombre": "Juan", "edad": 18, "salario": 11600},
{"nombre": "Sergio", "edad": 35, "salario": 18300},
{"nombre": "Alberto", "edad": 50, "salario": 19900}
]

promedio_edad = 0
menor_edad = 100

for usuario in usuarios:
    promedio_edad += usuario['edad']
    if usuario['edad'] < menor_edad:
        menor_edad = usuario['edad']

promedio_edad /= len(usuarios)

print(f'el promedio de edad es: {promedio_edad}')
print(f'la menor edad es: {menor_edad}')

df = pd.DataFrame(usuarios)
print(df['edad'])
print(df)
