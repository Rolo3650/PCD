# Invirtiendo una lista

lista = ['IPN', 'UNAM', 'ANAHUAC', 'TEC', 'IBERO', 2, 3, 4]

print(f'Lista original: {lista}')

lista.reverse()

print(f'Lista invertida: {lista}')

print(f'Lista original nuevamente: {lista[::-1]}')

print(f'Volvemos a invertirla: {list(reversed(lista))}')
