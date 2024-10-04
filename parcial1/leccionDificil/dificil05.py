import random
lambda_paridad = lambda n: 'Par' if n%2==0 else 'Impar'

lista = [random.randint(1,100) for i in range(5)]
print(lista)

for n in lista:
    print(f'{n} es {lambda_paridad(n)}')