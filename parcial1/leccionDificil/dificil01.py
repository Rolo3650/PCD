def masDeUnDato(x):
    return x, x**2, x**3

def loMismoPeroConListas(x):
    return [x, x**2, x**3]

x,x2,x3 = masDeUnDato(3)
lista = loMismoPeroConListas(3)

print(x,x2,x3)
print(lista)
