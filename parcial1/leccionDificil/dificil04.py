import math

lambda_pitagoras = lambda x,y: math.sqrt(x**2+y**2)
a=3
b=4
c=lambda_pitagoras(a,b)
print(f'La hipotenusa de un triangulo rectangulo')
print(f'Catetos a={a} y b={b}')
print(f'Hipotenusa c={c}')