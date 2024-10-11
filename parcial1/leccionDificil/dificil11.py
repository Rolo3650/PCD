import random
import functools

lambda_suma = lambda x,y: x+y    
print(f'Suma: {lambda_suma(3,5)}')

numeros = [random.randint(1,10) for _ in range(5)]
print(numeros)

s = functools.reduce(lambda_suma, numeros)

print(f'Promedio: {s/len(numeros)}')
