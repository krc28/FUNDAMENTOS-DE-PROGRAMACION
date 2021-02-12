"""listo
En un estacionamiento cobran $1.500 por hora o fracción. 
Diseñe un algoritmo que determine cuanto debe pagar un cliente por el estacionamiento de su vehículo, 
conociendo el tiempo de estacionamiento en horas y minutos.
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
horas = int(input("ingresa las horas de estacionamiento "))
minutos = int(input("ingresa los minutos de estacionamiento "))
costo = 1500
tiempo = costo * horas
if (minutos == 0):
   print (tiempo)
elif (minutos >= 1):
   print (tiempo + costo)