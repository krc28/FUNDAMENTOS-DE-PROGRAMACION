"""
Diseñe un algoritmo que lea un número de tres cifras y determine si es igual al revés del número.
Observación
Como el número tiene tres cifras, para que sea igual al revés, basta con que la cifra de las unidades sea igual a la cifra de las centenas. Por ejemplo: 353, 878, etc.
"""
numero = int (input ("ingrese el numero "))
centena = int (numero / 100)
unidad = int (numero % 10)
if (centena == unidad):
    print ("el numero es igual a su reves")
else:
    print ("el numero no es igual a su reves")