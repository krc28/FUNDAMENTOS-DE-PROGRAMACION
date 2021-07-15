"""
Diseñe un algoritmo que lea tres longitudes y determine si forman o no un triángulo.
Si es un triángulo determine de que tipo de triángulo se trata entre: equilátero (si tiene tres lados iguales), 
isósceles (si tiene dos lados iguales) o escaleno (si tiene tres lados desiguales).
Considere que para formar un triángulo se requiere que: "el lado mayor sea menor que la suma de los otros dos lados".
  """
longitud_uno = float (input ("ingrese la longitud del primer lado: "))
longitud_dos = float (input ("ingrese la longitud del segundo lado: "))
longitud_tres = float (input ("ingrese la longitud del tercer lado: "))
triangulo = (longitud_uno < (longitud_dos + longitud_tres)) and (longitud_dos < (longitud_uno + longitud_tres)) and (longitud_tres < (longitud_uno + longitud_dos))
equilatero = (longitud_uno == longitud_dos == longitud_tres)
isosceles = (longitud_uno == longitud_dos) or (longitud_uno == longitud_tres) or (longitud_dos == longitud_tres)
if (triangulo):
    print ("Las longitudes ingresadas forman un triángulo")
    if (equilatero):
        print ("El triángulo formado es equilatero")
    elif (isosceles):
        print ("El triángulo formado es isósceles")
    else:
        print ("El triángulo formado es escaleno")
else:
    print ("Las longitudes ingresadas no forman un triángulo")