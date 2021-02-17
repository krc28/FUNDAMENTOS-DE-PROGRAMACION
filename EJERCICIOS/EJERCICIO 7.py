"""
El promedio de prácticas de un curso se calcula en base a cuatro prácticas calificadas 
de las cuales se elimina la nota menor y se promedian las tres notas más altas.
Diseñe un algoritmo que determine la nota eliminada y el promedio de prácticas de un estudiante.
(int (promedio_notas) - int (nota_eliminada)) / 3
 """
nota1 = float (input ("ingrese la primera nota de práctica: "))
nota2 = float(input ("ingrese la segunda nota de práctica: "))
nota3 = float (input ("ingrese la tercera nota de práctica: "))
nota4 = float (input ("ingrese la cuarta nota de práctica: "))
primera_nota = (nota2 >= nota1) and (nota3 >= nota1) and (nota4 >= nota1)
segunda_nota = (nota1 >= nota2) and (nota3 >= nota2) and (nota4 >= nota2)
tercera_nota = (nota1 >= nota3) and (nota2 >= nota3) and (nota4 >= nota3)
cuarta_nota = (nota1 >= nota4) and (nota2 >= nota4) and (nota3 >= nota4)
promedio_notas = (nota1 + nota2 + nota3 + nota4)
if (primera_nota):
    nota_eliminada = nota1
    promedio = ((promedio_notas - nota_eliminada) / float (3))
    print ("la primera nota es la eliminada equivalente a: " + str (nota1))
elif (segunda_nota):
    nota_eliminada = nota2
    promedio = ((promedio_notas - nota_eliminada) / float (3))
    print ("la segunda nota es la eliminada equivalente a: " + str (nota2))
elif (tercera_nota):
    nota_eliminada = nota3
    promedio = ((promedio_notas - nota_eliminada) / float (3))
    print ("la tercera nota es la eliminada equivalente a: " + str (nota3))
else:
    (cuarta_nota)
    nota_eliminada = nota4
    promedio = ((promedio_notas - nota_eliminada) / float (3))
    print ("la cuarta nota es la eliminada equivalente a: " + str (nota4))
print ("el promedio de prácticas del estudiante es: " + str (promedio))