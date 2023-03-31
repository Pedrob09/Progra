""""
En Chile, si las personas que tienen menos de 18 años, son consideradas menores de edad; 
aquellas que están en el rango etario de 18 a 35 años se les considera adultos-jóvenes; 
quienes superan los 35 años, pero aún no alzanzan los 65 años, son consideradas adultos, 
y los que tiene 65 años o más son consideradas adultos mayores o miembros de la "tercera edad".

Se solicita que construya un programa en Python que solicite por teclado la edad de una persona 
e indique su categoría a partir del rango etario dado."""

edad = int(input("ingresar edad del paciente: "))

if edad < 18:
    print("el paciente es menor de edad")
elif edad < 35:
    print("el paciente es adulto-joven")
elif edad < 65:
    print("el paciente es adulto")
elif edad < 120:
    print("el paciente es mayor de edad")
else:
    print("probablemente el paciente esté muerto xd")
