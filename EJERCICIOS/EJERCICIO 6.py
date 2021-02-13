"""
Diseñe un algoritmo que determine quienes son contemporáneos entre Juan, Mario y Pedro.
 """
edad_j = int (input ("Juan ingrese su edad: "))
edad_m = int (input ("Mario ingrese su edad: "))
edad_p = int (input ("Pedro ingrese su edad: "))
if (edad_j == edad_m) and (edad_j == edad_p):
    print ("Juan, Mario y Pedro son contemporáneos")
elif (edad_j == edad_m) and (edad_j != edad_p):
    print ("Juan es contemporáneo de Mario pero no de Pedro")
    print ("Mario es contemporáneo de Juan pero no de Pedro")
    print ("Pedro no es contemporáneo con Juan y Mario")
elif (edad_m == edad_p) and (edad_m != edad_j):
    print ("Mario es contemporáneo de Pedro pero no de Juan")
    print ("Pedro es contemporáneo de Mario pero no de Juan")
    print ("Juan no es contemporáneo con Mario y Pedro")
elif (edad_p == edad_j) and (edad_p != edad_m):
    print ("Pedro es contemporáneo de Juan pero no de Mario")
    print ("Juan es contemporáneo de Pedro pero no de Mario")
    print ("Mario no es contemporáneo con Pedro y Juan")
else:
    print ("Juan, Mario y Pedro no son contemporáneos")