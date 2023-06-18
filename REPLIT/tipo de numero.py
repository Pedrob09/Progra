# TIPO DE NUMERO

# ENTRADA
numero = int(input())

# PROCESAMIENTO
acumulador = 0
divisor = 0

while divisor <= numero:
    divisor = divisor + 1
    if numero % divisor == 0:
        acumulador = acumulador + divisor
# SALIDA
if acumulador < 2 * numero:
    print("El número", numero, "es deficiente.")
elif acumulador == 2 * numero:
    print("El número", numero, "es perfecto.")
else:
    print("El número", numero, "es abundante.")
