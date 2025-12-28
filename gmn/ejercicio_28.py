# -*- coding: utf-8 -*-
# Ejercicio 28: Escribiendo y leyendo archivos

with open('archivo_de_prueba.txt', 'w', encoding='utf-8') as archivo:
    archivo.write("Reporte de Salarios: Finalizado el 9 de Diciembre.")
    
with open('archivo_de_prueba.txt', 'r', encoding='utf-8') as archivo:
    contenido_leido = archivo.read()
    
print(contenido_leido)
    
    