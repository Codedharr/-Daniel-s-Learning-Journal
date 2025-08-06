"""
Tipos de datos con Python: 

Tipo de dato numerico: Números enteros, números punto flotante, número complejos.
Tipo de dato booleano: 0 y 1 , True y false.
Tipo de dato cadena de texto (String): "Texto", 'Ejemplo'
Listas: son secuencias mutables de valores. lista = [1, 2, 3, 8, 9]
Tuplas: son secuencias inmutables de valores. tupla = (1, 4, 8, 0, 5)
Conjuntos: se utilizan para representar conjuntos únicos de elementos, es decir, en un conjunto no pueden existir dos objetos iguales. conjunto = set([1, 3, 1, 4])
Diccionarios: son tipos especiales de contenedores en los que se puede acceder a sus elementos a partir de una clave única. diccionario = {'a': 1, 'b': 3, 'z': 8}

"""

###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
city = "Valera"
name = "Daniel"
print(f"Bienvenido {name}\nVives en {city}")


print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

cadena = "12345"
flotante = 3.99
print(int(cadena))
print(float(cadena))
print(round(flotante))

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name = "Daniel"
age = "20"
hight = 1.80
print(f"Hola! Me llamo {name} y tengo {age} años, mido {hight} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1") 


division = int(round(3.14) / 2)
print(division)

