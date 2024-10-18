# Crear un programa que genere 100 numeros aleatorios entre 1 y 1000
# inserte en un alista los pares y en otr alos impares
# Imprimir ambas listas y el tamaño de las mismas
import random

listaA = [random.randint(1,1000) for i in range(100)]
listaP = []
listaI = []

for i in listaA:
    if (i % 2 == 0):
        listaP.append(i)
    else: 
        listaI.append(i)
        
print("Lista A:", listaA)
print("Lista P:", listaP)
print("Lista I:", listaI)