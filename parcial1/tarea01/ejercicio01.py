
import string

caracteres_ascii = string.ascii_letters
print(caracteres_ascii)

def verificar(cadena):
    # Escribe el codigo que verifique que todos los caracteres de una
    # cadena son letras ASCII
    # Devuelve: True en caso de que todos los caracteres sean letras ascii
    #           False en caso contrario
    
    for i in cadena: 
        valid = False
        for j in caracteres_ascii:
            if j == i: 
                valid = True
                break
        if valid == False: 
            return False
    return True


cadena1 = "Esto"
print(verificar(cadena1))