# Ejercicio 03 - Practicando con Claude

# 1. Crea una lista llamada `lenguajes` con 5 lenguajes de programación (strings)
lenguajes = ['Python', 'Java', 'C++', 'Ruby', 'R']

# 2. Imprime la lista completa
print(f'Lista original:{lenguajes}')

# 3. Imprime el primer elemento de la lista (índice 0)
print(f'Primer elemento: {lenguajes[0]}')

# 4. Imprime el último elemento usando índice negativo
print(f'Ultimo elemento: {lenguajes[-1]}')

# 5. Agrega un nuevo lenguaje al final usando `.append()`
lenguajes.append('Kotlin')
print(f'Adicion de lenguaje Kotlin a la lista: {lenguajes}')

# 6. Inserta "JavaScript" en la posición 2 usando `.insert()`
lenguajes.insert(2, 'JavaScript')
print(f'Adicion de lenguaje JavaScript a la tercera posicion: {lenguajes}')

# 7. Elimina el tercer elemento de la lista usando `.pop()`
lenguajes.pop(2)
print(f'remocion de tercer elemento a la lista: {lenguajes}')

# 8. Muestra la longitud final de la lista
print(f'la longitud de la lista Lenguajes es de : {len(lenguajes)}')

# 9. Imprime la lista ordenada alfabéticamente usando `.sort()`
lenguajes.sort()
print(f'Lista ordenada alfabeticamente: {lenguajes}')