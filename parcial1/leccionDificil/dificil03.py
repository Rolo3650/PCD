def cuadrado(x):
    # Esta funcion eleva al cuadrado el parametro x
    y = x**2
    return y

lambda_cuadrado = lambda x: x**2

print(f'Con def: {cuadrado(5)}')
print(f'Con funcion lambda: {lambda_cuadrado(5)}')