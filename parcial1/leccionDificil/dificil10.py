# Map
import random

lambda_cuadrado = lambda x: x**2

aleatorios = [random.random() for _ in range(5)]

print(aleatorios)
#print(lambda_cuadrado(3))
cuadrados1 = []
for x in aleatorios:
    #print(f'{x} : {lambda_cuadrado(x)}')
    cuadrados1.append(lambda_cuadrado(x))
    
print(cuadrados1)


cuadrados2 = list(map(lambda_cuadrado, aleatorios))
print(cuadrados2)
