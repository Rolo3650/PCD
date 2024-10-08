# Booleanos

a = True
b = False

print(type(a))

print(f'a={a}')

print(f'b={b}')

print(f'34 == 34 : {34==34}')

print(f'23 == 24: {23 == 24}')

print(f'34 != 34 : {34!=34}')

print(f'23 != 24: {23 != 24}')

x,y,z = 1,2,3

if x < y and y < z:
    print('x < y < z')
else:
    print('Error en el and')
    

if x > y or y < z:
    print('x > y  o  y < z')
else:
    print('Error en el or')


if not x > z:
    print('Negacion') 