# Mas Formato de cadenas con numeros
cadena1 = "{0:b}".format(13)
print("Binario del 256: ", cadena1)

cadena2 = "{0:e}".format(1234.34534535359379)
print("Formato exponencial: ", cadena2)

cadena3 = "{a:.4f}".format(a=3.141592)
print("Flotante truncado a 4 digitos: ", cadena3)

