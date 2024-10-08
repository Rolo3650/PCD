# Agregando a Listas

# Primero es una lista vacia
lista = []
print(f'Lista vacia: {lista}')

lista.append('IPN')
lista.append('UNAM')
lista.append('TEC')
lista.append('IBERO')

print(f'Universidades: {lista}')

for i in range(2,5):
    lista.append(i)
    
print(f'Lista con universidades y numeros: {lista}')

lista.insert(2, 'ANAHUAC')
print(f'Insertando un objeto: {lista}')

