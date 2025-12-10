import pandas as pd

datos_empresa = [
    {"nombre": "Maria", "departamento": "Ventas", "salario": 10300},
    {"nombre": "Pedro", "departamento": "IT", "salario": 15100},
    {"nombre": "Juan", "departamento": "Ventas", "salario": 11600},
    {"nombre": "Sergio", "departamento": "IT", "salario": 18300},
    {"nombre": "Alberto", "departamento": "Ventas", "salario": 19900}
]

df = pd.DataFrame(datos_empresa)
print(df)

df_suma_salarios = df['salario'].sum()
print(f'\nLa suma de los salarios es de: {df_suma_salarios}')

df_porgrupo = df.groupby('departamento')['salario'].mean()
print(f'\nEl salario promedio agrupado por departamento es:\n{df_porgrupo}')