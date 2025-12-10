# ejercicio 18.py

import pandas as pd

usuarios = [
{"nombre": "Maria", "edad": 30, "salario": 10300},
{"nombre": "Pedro", "edad": 25, "salario": 15100},
{"nombre": "Juan", "edad": 18, "salario": 11600},
{"nombre": "Sergio", "edad": 35, "salario": 18300},
{"nombre": "Alberto", "edad": 50, "salario": 19900}
]

df = pd.DataFrame(usuarios)

promedio_edad_pd = df['edad'].mean()
menor_edad_pd = df['edad'].min()

print(f'el promedio de edad es: {promedio_edad_pd}')
print(f'la menor edad es: {menor_edad_pd}')


