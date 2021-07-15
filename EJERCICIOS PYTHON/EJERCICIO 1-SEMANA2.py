"""
Elabore programa en Python que lea una temperatura en grados kelvin, la convierta a grados Fahrenheit 
y muestre el resultado con un mensaje bien explicativo.
No use aproximaciones
"""
Temperatura = float (input("Ingrese la temperatura: ")) 
Temperatura_kelvin = Temperatura + 273.15
Temperatura_fahrenheit = ((Temperatura_kelvin - 273.15)* 9/5) + 32
print ("La temperatura ingresada convertida a grados Fahrenheit es:",Temperatura_fahrenheit)