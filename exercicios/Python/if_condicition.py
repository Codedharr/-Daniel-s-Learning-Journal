###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("!------------------!")

num01 = input('Ingrese un número entero\n')
num02 = input('Ingrese otro número entero\n')

if num01 > num02: 
    print(f'El primer número registrado {num01} es mayor que {num02}')
else:
    print(f'El segundo número registrado {num02} es mayor que {num01}')


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("!------------------!")

num01 = float(input('Ingrese un número\n'))
num02 = float(input('Ingrese otro número\n'))
operacion = input("Introduce la operación (+, -, *, /):\n")

if operacion == "+":
    resultado = num01 + num02
elif operacion == "-":
    resultado = num01 - num02
elif operacion == "*":
    resultado = num01 * num02
elif operacion == "/":
    if  num01 == 0 or num01 == 0: 
        print('La divisio entre cero no es posible')
    else: 
        resultado = num01 / num02
else:
    print('La operación no es posible')


if 'resultado' in locals():
    print(f"El resultado es: {resultado}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.


anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")



print("!------------------!") 

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)


edad = int(input('Ingrese su edad: \n'))

if edad <= 2:
    print('Ud es un Bebé')
elif edad <= 12: 
        print('Ud es un niño')
elif edad <= 17: 
    print('UId es un adolescente')
elif edad <= 64: 
    print('Ud es un adulto')
else: 
    print('Ud es un adulto')



print("!------------------!")
