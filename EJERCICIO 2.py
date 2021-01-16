"""
Diseñe un algoritmo que determine si ún número es o no es, par positivo.
"""
"""
INICIO
var numero
mostrar "escriba numero"
leer numero
if (numero % 2 == 0)
    print ("es par")
else 
    print ("es impar")
    FIN IF
FIN
"""
numero = input ("ingresa el numero:")
dato = int(numero) % 2
if (dato == 0):
    print ("el numero es par")
else:
    print ("el numero es impar")