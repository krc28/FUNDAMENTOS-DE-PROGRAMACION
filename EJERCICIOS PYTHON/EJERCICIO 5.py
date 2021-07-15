"""listo
Una compañía dedicada al alquiler de automoviles cobra un monto fijo de $300000 para los primeros 300 km de recorrido.
 Para más de 300 km y hasta 1000 km, cobra un monto adicional de $ 15.000 por cada kilómetro en exceso sobre 300. 
 Para más de 1000 km cobra un monto adicional de $ 10.000 por cada kilómetro en exceso sobre 1000. 
 Los precios ya incluyen el 20% del impuesto general a las ventas, IVA.  Diseñe un algoritmo que determine el monto a pagar por el alquiler de un vehículo y el monto incluído del impuesto.
 """
recorrido = int (input ("ingrese los kilometros recorridos:"))
monto_inicial = 300000
monto_adicional_hasta_mil_km = ((recorrido - 300) * 15000 + monto_inicial)
monto_adicional_desde_mil_km = ((recorrido - 1000) * 10000 + monto_inicial) + (700 * 15000)
km_inicial = 300
km_adicional = 1000
porcentaje = 0.20
if (recorrido <= km_inicial):
    monto = int (monto_inicial * porcentaje)
    monto_final = monto_inicial
elif (recorrido > km_inicial) and (recorrido <= km_adicional):
    monto = int (monto_adicional_hasta_mil_km * porcentaje)
    monto_final = monto_adicional_hasta_mil_km
else:
    monto = int (monto_adicional_desde_mil_km * porcentaje)
    monto_final = monto_adicional_desde_mil_km
print ("monto del IVA:" + str(monto))
print ("el monto a pagar por el alquiler del vehiculo IVA incluido es:" + str(monto_final))