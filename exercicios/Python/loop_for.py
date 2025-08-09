cadana = [1,2,3,4,5,6,7,8,9,10]

for index in cadana:
    print(index)


frutas = ['manzana', 'cebolla', 'zanahoria', 'tomate']

for index, fruta in enumerate(frutas): 
    print(f'El indice es {index} y la fruta es: {fruta}')

numeros = [print(caracter) for caracter in cadana]



###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = [num for num in numeros if num % 2 == 0]
print(pares)


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
media = 0
numeros = [10, 20, 30, 40, 50]
for num in numeros:
    media += num

media = media // len(numeros)
print(media)

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

numeros = [15, 5, 25, 10, 20]
maximo = 0
for nums in numeros: 
    if nums > maximo:
        maximo = nums

print(f'El número mayor es: {maximo}')
    

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
print(palabras_largas)
