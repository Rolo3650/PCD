#List comprehension
import random

x = [random.randint(1,100) for _ in range(10)]
print(f'Numeros aleatorios: {x}')
