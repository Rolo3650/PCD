# Eliminando elementos de un alista

lista = [1, 2, 3, 4, 2, 2, 5, 6, 2, 7]

print(f'Lista original: {lista}')

lista.remove(2)
lista.remove(6)

print(f'Se eleimino un elemento: {lista}')

x = lista.pop()

print(f'Se extrajo el ultimo elemento: {x} de la lista: {lista}')
