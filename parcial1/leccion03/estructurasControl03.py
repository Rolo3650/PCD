# If

def comparar(i):
    if (i > 0):
        return 'Positivo'
    elif (i < 0):
        return 'Negativo'
    else:
        return 'Cero'

lambda_comparar1 = lambda i: {i>0: 'Positivo', i <0: 'Negativo'}.get(True, "Cero")

lambda_comparar2 = lambda i: 'Positivo' if i > 0 else ('Negativo' if i<0 else 'Cero')

    
for i in range(-2,3,1):
    print(f'Def: {i} es {comparar(i)}')
    

for i in range(-2,3,1):
    print(f'Lambda1: {i} es {lambda_comparar1(i)}')

for i in range(-2,3,1):
    print(f'Lambda2: {i} es {lambda_comparar2(i)}')
