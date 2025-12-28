import pandas as pd

# DataFrame 1: Datos de la Empresa (ya creado)
datos_empresa = [
    {"nombre": "Maria", "departamento": "Ventas", "salario": 10300},
    {"nombre": "Pedro", "departamento": "IT", "salario": 15100},
    {"nombre": "Juan", "departamento": "Ventas", "salario": 11600},
    {"nombre": "Sergio", "departamento": "IT", "salario": 18300},
    {"nombre": "Alberto", "departamento": "Ventas", "salario": 19900}
]
df = pd.DataFrame(datos_empresa)

# DataFrame 2: Datos de Antigüedad (Nueva Fuente)
datos_antiguedad = [
    {"nombre": "Maria", "antiguedad_anos": 7},
    {"nombre": "Pedro", "antiguedad_anos": 2},
    {"nombre": "Juan", "antiguedad_anos": 1},
    {"nombre": "Sergio", "antiguedad_anos": 10},
    {"nombre": "Alberto", "antiguedad_anos": 15}
]
df2 = pd.DataFrame(datos_antiguedad)

df_antiguedad = pd.merge(df, df2, on="nombre") 
print(df_antiguedad)