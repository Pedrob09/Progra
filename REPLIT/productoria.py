# PRODUCTORIA

# ENTRADA
n = input('Ingrese un valor: ')
# PROCESAMIENTO
n = int(n)
if n >= 1:
    i = 1
    acumulador = 1
    while i <= n:
        acumulador = acumulador * i
        i = i + 1
# SALIDA
    print('La productoria desde 1 hasta', n, 'es:', acumulador)
