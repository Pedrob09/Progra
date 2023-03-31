""""
Diseñe un programa que solicite por teclado la edad de 2 personas e indique quién es el más joven. 
Tener en consideración que ambas personas pueden tener la misma edad, 
por lo que se debe generar un mensaje adecuado para cada caso
"""
edad_1 = int(input("ingresar edad del primer paciente: "))
edad_2 = int(input("ingresar edad del segundo paciente: "))

if edad_1 < edad_2:
    print("el primer paciente es menor al segundo paciente")
else:
    print("el segundo paciente es menor al primero")

if edad_1 == edad_2:
    print("los pacientes tienen la misma edad")
