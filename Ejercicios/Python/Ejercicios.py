# Ejercicio 1: Conversor de Temperatura
# Escribe un programa que convierta una temperatura de grados Celsius a grados
# Fahrenheit.

""""
print("Que temperatura quiere convertir to F")
inputC = int(input("Introduza la temperatura: "))

ConversionF = 32
ConversionTotal = inputC * 9 / 5 + ConversionF
print(ConversionTotal)


# Ejercicio 2: Calculadora de Propina
# Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
# una propina del 15% sobre el total de la cuenta.
#cuenta = 10
Propina = 0.15
CalculoTotal = (Cuenta * Propina) + Cuenta
print(CalculoTotal)


# Ejercicio 3: Verificación de Edad
# Escribe un programa que solicite la edad de un usuario y determine si es mayor de
# edad (mayor o igual a 18 años) o no.
x = 22
if x > 18:
    print("Es mayor de 18 años")
elif x <= 18:
    print("Es menor de 18 años")

# Ejercicio 4: Contador de Vocales
# Crea un programa que cuente el número de vocales en una palabra ingresada por el
# usuario.
inputlen = "Armando"
print(len(inputlen))

# Ejercicio 5: Suma de Números Pares
# Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
# Inicializamos una variable para almacenar la suma

suma = 0
for num in range(1, 101):
    if num % 2 == 0:
        suma = suma + num
print("La suma de todos los números pares del 1 al 100 es:", suma)

# Ejercicio 6: Verificación de Palíndromo
# Crea un programa que verifique si una palabra ingresada por el usuario es un
# palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()
palabra_sin_espacios = palabra.replace(" ", "")
palabra_invertida = palabra_sin_espacios[::-1]
if palabra_sin_espacios == palabra_invertida:
    print("Si, es un palíndromo")
else:
    print("No, no es un palíndromo")

# Ejercicio 7: Calculadora Simple
# Crea un programa que realice operaciones aritméticas simples (suma, resta,
# multiplicación, division) según la elección del usuario.


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion = input("Seleccione una operación (1/2/3/4): ")

if opcion in ("1", "2", "3", "4"):
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if opcion == "1":
        print("Resultado:", suma(num1, num2))
    elif opcion == "2":
        print("Resultado:", resta(num1, num2))
    elif opcion == "3":
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == "4":
        print("Resultado:", division(num1, num2))
else:
    print("Opción inválida")

#Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
#Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print("Su Índice de Masa Corporal (IMC) es:", imc)

#Ejercicio 9: Conversor de Divisas
#Ejercicios Introducción a Python: Enunciados 2
#Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
#1 dólar es igual a 0.85 euros.

def calcular_cambio(dolares):
    return dolares / 1.25
dolares = float(input("Cuantos dolares tienes: "))
cambio = calcular_cambio(dolares)
print(cambio)



# Ejercicio 10: Determinar el Día de la Semana
# Escribe un programa que determine el día de la semana correspondiente a un
# número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
def determinar_dia_semana(numero):
    dias_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo",
    }
    if numero in dias_semana:
        return dias_semana[numero]
    else:
        return "Número de día no válido"


numero = int(input("Ingrese un número del 1 al 7: "))

print("El día correspondiente al número ingresado es:", determinar_dia_semana(numero))

# Ejercicio 11: Calculadora de Edad
# Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
# actual.
from datetime import date

hoy = date.today()
numero = int(input("Ingrese su fecha de nacimiento: "))

if len(str(numero)) != 4:
    print("Estas metiendo la fecha mal")
else:
    nacimiento = hoy.year - numero
    print(nacimiento)

# Ejercicio 12: Calculadora de Área de un Rectángulo
# Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
# longitud y el ancho del rectángulo.


def calcular_area_rectangulo(longitud, ancho):
    return longitud * ancho
longitud = float(input("Ingrese la longitud:"))
ancho = float(input("Ingrese el ancho:"))

area = calcular_area_rectangulo(longitud, ancho)
print(area)

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Verificar si el número ingresado es primo llamando a la función es_primo
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")



def calcular_descuento(precio, descuento):
    return precio * (1 - descuento / 100)


precio = float(input("Ingrese el precio:"))
descuento = float(input("Ingrese el descuento:"))

precio_final = calcular_descuento(precio, descuento)
print(precio_final)


# Ejercicio 15: Conversor de Tiempo
# Escribe un programa que convierta un número de minutos en horas y minutos. Por
# ejemplo, 145 minutos serían 2 horas y 25 minutos.


def calcular_tiempo(tiempo):
    horas = tiempo // 60
    minutos = tiempo % 60
    return horas, minutos

tiempo = float(input("Ingrese los minutos que quieres convertir a horas: "))
minutos, horas = calcular_tiempo(tiempo)
print(f"{minutos} minutos son {horas} horas y {calcular_tiempo(tiempo)} minutos.")



# Ejercicio 16: Contador de Números Pares e Impares
# Crea un programa que cuente y muestre la cantidad de números pares e impares en
# una lista ingresada por el usuario.
def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares


numeros = input("Ingrese una lista de números separados por espacio: ").split()
# Convertir los números a enteros
numeros = [int(numero) for numero in numeros]
# Llamar a la función contar_pares_impares para obtener el resultado
pares, impares = contar_pares_impares(numeros)
# Imprimir el resultado
print(f"La lista contiene {pares} números pares y {impares} números impares.")


# Ejercicio 17: Conversor de Millas a Kilómetros
# Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
# que 1 milla equivale a 1.60934 kilómetros.


def calculodistancia(distancia):
    conversion = 1.60934 * distancia
    return conversion

distancia = int(input("Ingrese la distancia a convertir en millas: "))
conversion = calculodistancia(distancia)
print(conversion)



# Ejercicio 18: Contador de Palabras
# Ejercicios Introducción a Python: Enunciados 3
# Crea un programa que cuente la cantidad de palabras en una oración ingresada por
# el usuario.
def cuenta(distancia):
    palabras = distancia.split()
    totalcuenta = len(palabras)
    return totalcuenta
distancia = input("Escribe una frase y te contare: ")
totalcuenta = cuenta(distancia)
print(totalcuenta)



# Ejercicio 19: Verificación de Año Bisiesto
# Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
# no.


def bisiesto(año):
    if año % 4 == 0:
        return True
    else:
        return False
año = int(input("Pon un año y te dire si es bisiesto:"))
año = bisiesto(año)

if año:
    print("Es un año bisiesto")
else:
    print("No lo es")
"""
# Ejercicio 20: Suma de Números en una Lista
# Crea un programa que sume todos los números en una lista ingresada por el
# usuario.


def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma


# Solicitar al usuario que ingrese una lista de números separados por espacio
numeros = input("Ingrese una lista de números separados por espacio: ").split()
# Convertir los números a enteros
numeros = [int(numero) for numero in numeros]
# Llamar a la función suma_lista para obtener la suma de los números
resultado_suma = suma_lista(numeros)
# Imprimir el resultado
print("La suma de los números en la lista es:", resultado_suma)
