# Filter 
import random

listaNumeros = [random.randint(1, 100) for _ in range(10)]
print(listaNumeros)

lambda_esPar = lambda x: True if x%2 == 0 else False

pares = []
for x in listaNumeros:
    #print(x, lambda_esPar(x))
    if lambda_esPar(x) == True:
        pares.append(x)
        
print(f'Pares: {pares}')


pares2 = list(filter(lambda_esPar, listaNumeros))
print(f'Pares filtrados: {pares2}')