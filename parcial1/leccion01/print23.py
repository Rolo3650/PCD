# argumentos por posicion y por nombre
print('El mejor equipo {0}, el segundo {1}, y el tercero {otro}.'
     .format('CELTICS', 'NUGGETS', otro ='BULLS'))

# con format, posiciones y formato
print("Primera posicion, entero de un digito:>>{0:3d}<<, segunda posicion flotante:>>{1:8.2f}<<".
      format(12, 00.546))

# Cambiando posiciones
print("segundo argumento flotante:>>{1:8.2f}<< primer argumento entero:>>{0:3d}<<, ".
      format(12, 00.546))

# Argumentos por nombre
print("a: {a:5d},  Portbal: {b:8.2f}".
     format(a = 1234, b = 19.123456789))