# -*- coding: utf-8 -*-

# Juego de adivinar números.

# Se importa la función randint del módulo random.
from random import randint

# Se elige un número aleatorio, generado por la función randint.
NUMERO_ALEATORIO = randint(1,50)

# Algo de información.
print("      Juego de la adivinanza de números")
print("--------------------------------------------")
print("Elige un número entre el 1 y el 50.")
print("Para salir en cualquier momento introduce 0.")

print("\n")
    
print(NUMERO_ALEATORIO)

intentos = 0
opcion = 0
while True:
    intentos += 1
    opcion = int(input("Adivina el número....: "))
    if abs(NUMERO_ALEATORIO - opcion) > 25:
        print("Estás helado... no te acercas ni de casualidad")
    elif 15 < abs(NUMERO_ALEATORIO - opcion) <= 25:
        print("Sigues lejos... afina colega!")
    elif 10 < abs(NUMERO_ALEATORIO - opcion) <= 15:
        print("Te estás quemando ... vas por buen camino!!!")
    elif 5 < abs(NUMERO_ALEATORIO - opcion) <= 10:
        print("Uff... que cerca estás de adivinar el número!!!")
    elif 1 < abs(NUMERO_ALEATORIO - opcion) <= 5:
        print("Maaaaadre mía... que lo aciertas!!!")
    elif 1 == abs(NUMERO_ALEATORIO - opcion):
        print("¡¡¡Que me va a dar un infartooooo!!!")
    elif NUMERO_ALEATORIO == opcion:
        print("HAS ACERTADO!!! Has necesitado %d intentos" % intentos)
        break
      
      
      
