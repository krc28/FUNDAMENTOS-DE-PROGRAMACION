"""listo
Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% 
por la compra de más de 3 docenas y 10% en caso contrario. Además por la compra de más de 3 docenas se obsequia una 
unidad del producto por cada docena en exceso sobre 3. Diseñe un algoritmo que determine el monto de la compra, 
el monto del descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto. 
"""
unidades_de_producto = int(input("ingrese la cantidad de unidades de producto compradas por el cliente "))
precio_del_producto = int(input("ingrese el precio del producto "))
monto_de_la_compra = precio_del_producto * unidades_de_producto
if (unidades_de_producto <= 35):
    porcentaje = 0.10
    unidades_de_obsequio = 0
else:
    porcentaje = 0.15
    unidades_de_obsequio = int(unidades_de_producto / 12) - 3
monto_del_descuento = monto_de_la_compra * porcentaje
print ("precio sin descuento " + str(monto_de_la_compra))
print ("monto del descuento " + str(monto_del_descuento)) 
print ("monto a pagar " + str(monto_de_la_compra - monto_del_descuento))
print ("unidades a obsequiar " + str(unidades_de_obsequio)) 