# Conteo regresivo con y sin flush

import time

count_seconds = 5
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        #Intenta primero con esta linea
        #print(i, end='>>>')
        #Despues comenta la linea anterior y descomenta la siguiente
        print(i, end='>>>', flush = True)
        time.sleep(3)
    else:
        print('Inicio')