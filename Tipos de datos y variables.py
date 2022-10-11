from decimal import Clamped
from re import A


#CLASE 29/09/2022

#Tipos de datos y variables

#Numéricos
#Enteros -- int
#Real -- float
#Cadenas de carácteres -- str
#Lógico -- bool

nombre = "Raúl"
edad = 17
mayor_O_menor_edad = False  
print(type(mayor_O_menor_edad))

# Entrada y salida de datos
#Salida con print()
print("Buenos días", (nombre), "Tu edad es", (edad))

#Entrada de datos -- input()

nombre = input("Dime tu nombre:\n ")
edad = input("Dime tu edad:\n ")
print("Buenos días", (nombre), "tu edad es", (edad))

#Bucle while

i = 0
bandera = True
while (bandera == True):
    print("No has esto nunca", i)
    i = i+1
    if (i==30000):
        bandera = False