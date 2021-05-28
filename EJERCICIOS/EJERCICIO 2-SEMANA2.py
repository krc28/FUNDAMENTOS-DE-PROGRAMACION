"""
Elabore un programa en Python que lea un entero de tres dígitos y produzca como salida los dígitos 
del número leído con su correspondiente mensaje. Por ejemplo, si el número leído es 271, 
la salida deberá ser (sin texto adicional):
2
7
1 
"""
Numero = int(input("Ingrese el número de tres dígitos: "))
Uno = int (Numero / 100)
Dos = int ((Numero % 100) / 10)
Tres = int (Numero % 10)
print(Uno,"\n",Dos,"\n",Tres)