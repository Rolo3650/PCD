cadena1 = '3l s3ñ0r d3 l0s 4n1ll0s'
print(cadena1)
print(''.join(['a', 'b', 'c']))
x= '3'
print(x.isdigit())
z='s'
print(z.isdigit())
c2 = 'hola'
for c in c2:
    print(c)
print('FIN')

def sinNumeros(cadena):
    nuevaCadena=''
    for c in cadena:
        if not c.isdigit():
            nuevaCadena = nuevaCadena + c
    return nuevaCadena

lambda_sinnumeros = lambda cadena: ''.join([c for c in cadena if not c.isdigit()])

lambda_solonumeros = lambda cadena: ''.join([c for c in cadena if c.isdigit()])

print(f'cadena sin numeros: {sinNumeros(cadena1)}')
print(f'Lambda sin numeros: {lambda_sinnumeros(cadena1)}')
print(f'Lambda solo numeros: {lambda_solonumeros(cadena1)}')
