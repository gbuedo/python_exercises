# -*- coding: utf-8 -*-

# Ejercicio 4: Estucturas condicionales (if/then/else)

print("Tamaño")  # dentro de strings funciona mejor

# Variables
tamano_datos_mb = 10001

# Logica condicional
print(f"El tamano en datos es de: {tamano_datos_mb} MB")
if tamano_datos_mb < 100:
    print("Dataset pequeño - Se puede procesar en memoria")
elif tamano_datos_mb < 1000:
    print("Dataset mediano - Considerar optimizaciones")
elif tamano_datos_mb < 10000:
    print("Dataset grande - Usar procesamiento por chunks")
else:
    print("Dataset muy grande - Considerar Spark o Dask")

if tamano_datos_mb == 1000:
    print("Tamaño crítico detectado")