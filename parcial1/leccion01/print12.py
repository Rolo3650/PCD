# Como imprimir la fecha de hoy

import datetime

hoy = datetime.datetime.today()
print(f"{hoy: %B %d, %Y}")
print(f"{hoy: %m %d, %Y}")
