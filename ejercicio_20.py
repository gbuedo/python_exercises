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

# 1. Definición de la Máscara Booleana (Qué filas cumplen)
condicion = df['salario'] > 15000

# 2. Aplicar la Máscara al DataFrame completo (df[máscara])
df_alto_salario = df[condicion]

# 3. Calcular el promedio sobre la columna filtrada
promedio_nuevo_salario = df_alto_salario['salario'].mean()

# nuevo requisito
df_jovenes_ricos = df[(df['salario'] > 15000) & (df['edad'] < 40)]

print("\n--- DataFrame Filtrado (Usuarios con salario > 15000) ---")
print(df_alto_salario)
print("\n--- Resultado del Calculo ---")
print(f'El promedio de salario de este grupo es: {promedio_nuevo_salario:.2f}')
print(f'los usuarios jovenes y ricos son: \n{df_jovenes_ricos}')
