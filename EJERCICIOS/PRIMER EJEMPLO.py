"""print ("hola soy pochinki")
culo = "grande"
tetas = 2
print (culo + str(tetas))
estatura = int(input("ingresa tu estatura:"))
if (estatura >= 180):
    print("eres alto")
elif (estatura == 155):
    print ("eres pochinki")
else:
    print ("eres enano")"""
V = [8, 3, 1, 6, 2, 7, 4, 9, 5]
for i in range(1, 5):
    a = V[i]
    V[i] = V[8-i+1]
    V[8-i+1] = a
for i in range(0, 8):
    print(V[i], end="", sep=",")

 





