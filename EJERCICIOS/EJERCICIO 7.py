"""
El promedio de prácticas de un curso se calcula en base a cuatro prácticas calificadas 
de las cuales se elimina la nota menor y se promedian las tres notas más altas.
Diseñe un algoritmo que determine la nota eliminada y el promedio de prácticas de un estudiante.
 """
nota_uno = str (input ("ingrese la primera nota de práctica: "))
nota_dos = str (input ("ingrese la segunda nota de práctica: "))
nota_tres = str (input ("ingrese la tercera nota de práctica: "))
nota_cuatro = str (input ("ingrese la cuarta nota de práctica: "))
primera_nota = str ((nota_dos >= nota_uno) and (nota_tres >= nota_uno) and (nota_cuatro >= nota_uno))
segunda_nota = str ((nota_uno >= nota_dos) and (nota_tres >= nota_dos) and (nota_cuatro >= nota_dos))
tercera_nota = str ((nota_uno >= nota_tres) and (nota_dos >= nota_tres) and (nota_cuatro >= nota_tres))
cuarta_nota = str ((nota_uno >= nota_cuatro) and (nota_dos >= nota_cuatro) and (nota_tres >= nota_cuatro))
if (primera_nota):
    nota_eliminada = primera_nota
    promedio_notas = int ((nota_uno + nota_dos + nota_tres + nota_cuatro - nota_eliminada)) / 3
    print ("la primera nota es la eliminada equivalente a: " + nota_uno)
elif (segunda_nota):
    nota_eliminada = segunda_nota
    promedio_notas = int ((nota_uno + nota_dos + nota_tres + nota_cuatro - nota_eliminada)) / 3
    print ("la segunda nota es la eliminada equivalente a: " + nota_dos)
elif (tercera_nota):
    nota_eliminada = tercera_nota
    promedio_notas = int ((nota_uno + nota_dos + nota_tres + nota_cuatro - nota_eliminada)) / 3
else:
    (cuarta_nota)
    nota_eliminada = cuarta_nota
    promedio_notas = int ((nota_uno + nota_dos + nota_tres + nota_cuatro - nota_eliminada)) / 3
    print ("la cuarta nota es la eliminada equivalente a: " + nota_cuatro)
print ("el promedio de prácticas del estudiante es: " + promedio_notas)