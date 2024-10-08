# Slicing

lista = [i for i in range(100,1100, 100)]

print(f'Lista original: {lista}')

print(f'Slice de 0 a 9: {lista[0:len(lista)]}')

print(f'Slice de 0 a 2: {lista[0:3]}')

print(f'Slice de Inicio a 2: {lista[:3]}')

print(f'Slice de 3 a 9: {lista[3:10]}')

print(f'Slice de 3 al final: {lista[3:]}')

print(f'Slice de 4 a 6: {lista[4:7]}')

print(f'Slice de Inicio a Fin: {lista[:]}')

print(f'Slice posiciones pares: {lista[::2]}')

print(f'Slice posiciones impares: {lista[1::2]}')

print(f'Slice invertido impares: {lista[-1::-2]}')

print(f'Slice invertido pares: {lista[-2::-2]}')
