
lista = [1,2,3,4]
print(sum(lista))

cadena1 = 'abc1de2fghi3jklm4'

def sumarDigitos(cadena):
    suma = 0
    for c in cadena:
        if c.isdigit():
            suma = suma + int(c)
    return suma

lambda_sumardigitos = lambda cadena: sum([int(c) for c in cadena if c.isdigit()])

print(f'Sumar digitos: {sumarDigitos(cadena1)}')
print(f'Sumar digitos con lambdas: {lambda_sumardigitos(cadena1)}')
