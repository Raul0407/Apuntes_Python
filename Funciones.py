#Funciones

'''
edad = 5
edad_como_texto = str(edad)
edad = int(edad_como_texto)
print(edad*5)
print(len("Raúl"))
edad2 = int(input("Dime tu edad:\n"))
'''

#Funciones definidas por el usuario

def imprimirHola(nombre:str, apellido:str):
    print("Hola", nombre, apellido)

imprimirHola("Juan", "Zamora")

def imprimirSuma(numero1:int, numero2:int):
    print("La suma es:", numero1+numero2)
    return(numero1+numero2)

imprimirSuma(int(input()),int(input()))

suma = imprimirSuma(2,2)
print("La suma es:", suma)