#Listas en python

import re


vNombres = []

#Insertar un dato

vNombres.insert(0,"Juan")
vNombres.insert(1,"Pepe")
vNombres.insert(2,"Inés")
vNombres.append("Minerva")
vNombres.insert(1,"Julian")

#Eliminar un elemento

vNombres.remove("Pepe")
print("El nombre borrado es ", vNombres.pop(1))

#Ordenar una lista

vNombres.sort(reverse=False)   

#Contar elementos de la lista

print("El número de veces que aparece Inés es: ", vNombres.count("Inés"))
print("La lista tiene: ", len(vNombres), "elementos")

print(vNombres)