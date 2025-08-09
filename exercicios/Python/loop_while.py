###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

numeros = 0
while numeros <= 10:
    numeros += 1 
    print(numeros)

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

numeros_02 = 0
suma = 0
while numeros_02 < 20:
    numeros_02 += 1
    if numeros_02 % 2 == 0:
        suma += numeros_02

print(f'La suma de los numeros pares es: {suma}')

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

numero_factorial = int(input('Ingrese un número para encontrar su factorial:  '))
factorial = 1
while  numero_factorial > 0: 
    factorial *= numero_factorial
    numero_factorial -= 1


print(f'El numero factorial es: {factorial}')


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

while True:
    clave = input('Ingrese la clave: ')
    if len(clave) < 8: 
        print('La clave es invalida. Vuelva a intentar')
    else: 
        print('La clave es valida.')
        break

