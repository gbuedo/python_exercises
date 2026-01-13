# Ejercicio 05 - Bucles (for y while)

# Variables
volumenes_datos = [120, 450, 890, 1500, 250] # Representan en MB
total = 0
volumen = 0
contador = 0

for volumenes in volumenes_datos:
    print(f'Volumen {volumen}: {volumenes} MB')
    volumen += 1
    total = sum(volumenes_datos)

print(f'El total de volumenes de datos es: {total} MB')

while contador <= 1000:
    print(f'Contador: {contador} MB')
    contador += 100    

print('Se ha superado el limite de 1000 MB, se descartan 1000 MB')