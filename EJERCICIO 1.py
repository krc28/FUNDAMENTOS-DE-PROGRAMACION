"""
En un estacionamiento cobran $1.500 por hora o fracción. 
Diseñe un algoritmo que determine cuanto debe pagar un cliente por el estacionamiento de su vehículo, 
conociendo el tiempo de estacionamiento en horas y minutos.
"""
"""
se que vale 1500 la hora o la fraccion, entonces tiene que subir el precio por cada hora y cada fracción
pero no se como poner lo de que suba en cada fracción osea algo como que si los minutos son 15,30 y 45 aumente
en 1 la cantidad osea sume una vez mas los 1500. lo otro es que en pseudocodigo se pone es lea los datos y no como preguntarle
a la persona y luego ahi si que lea esos datos me enredo en cuando saber si debe ser cadena de texto o
una variable que lea y asi pueda arrojar los resultados
"""
"""
INICIO
 hora = numero de horas + 1 hora adicional dado que haya fracciones en el tiempo por los minutos
 minutos = numero de minutos creo
 costo = 1.500
 Leer hora_y_minutos
 if (minutos > "0"): no se si el cero si van en comillas o necesita ser leido ese dato de la variable establecida
    hora = (costo * hora) aqui no se como referirme o construir lo de que la hora es la cantidad de horas sumado las fracciones de hora que puedan aumentar el precio y luego 
    ahi si para dar el resultado final se mira lo que eso de por el costo establecido de 1500
  
 elif (minutos < "0"): no se si el cero si van en comillas o necesita ser leido ese dato de la variable establecida
    print (hora * costo)
 FIN IF
FIN   
"""
costo = 1.500 
horas = 0 + 1 
print ("ingresa el tiempo de estacionamiento")
horas = input("horas:")
minutos = input("minutos:") 
