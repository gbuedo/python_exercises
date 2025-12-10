# -*- coding: utf-8 -*-
# Ejercicio 27: Manejo de excepciones al dividir números

def dividir_numeros(a, b):
    try:
        return a / b 
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero. Devolviendo 0.")
        return 0
    except TypeError:
        print("Error de tipo: Asegúrate de usar solo números.")
        return None
    
Resultado_valido = dividir_numeros(10, 2)
Resultado_invalido = dividir_numeros(10, 0)
Resultado_tipo = dividir_numeros(10, 'a')

print(f"Resultado valido: {Resultado_valido}")
print(f"Resultado invalido: {Resultado_invalido}")
print(f"Resultado tipo: {Resultado_tipo}")
    