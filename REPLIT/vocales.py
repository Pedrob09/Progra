# VOCALES
# ENTRADA
frase = input('Ingrese una frase: ')
# PROCESAMIENTO
frase = frase.lower()
i = 0
acumulador = 0
while i < len(frase):
    if frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u':
        acumulador = acumulador + 1
    i = i + 1
# SALIDA
print('La cantidad de vocales en la frase es:', acumulador)

