# CONJETURA DE COLLATZ

# ENTRADA
numero = int(input())

# PROCESAMIENTO Y SALIDA
print(numero)

while numero > 1:
    if numero % 2 == 0:
        numero = numero / 2
        print(int(numero))
    else:
        numero = numero * 3 + 1
        print(int(numero))
