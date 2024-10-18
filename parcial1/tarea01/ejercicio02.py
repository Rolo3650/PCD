import string
import random

minusculas_ascii = string.ascii_lowercase
print(minusculas_ascii)

mayusculas_ascii = string.ascii_uppercase
print(mayusculas_ascii)

numeros = string.digits
print(numeros)


def generarPassword(n):
    # Escribe una funcion que genere un password aleatorio de n caracteres
    # el password debe contener letras mayusculas minusculas y numeros
    randType = random.randint(0, 2)
    if randType == 0: 
        return minusculas_ascii[random.randint(0, len(minusculas_ascii) - 1)]
    if randType == 1:
        return minusculas_ascii[random.randint(0, len(mayusculas_ascii))]
    if randType == 2:
        return numeros[random.randint(0, len(numeros) - 1)]

for i in range(10, 20):
    print(generarPassword(i), end = "")