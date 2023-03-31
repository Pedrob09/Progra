n = int(input("ingresar el numero n =" ))
numero_a_sumar = 1
ultimo_numero = 0
while ultimo_numero <= n:
    ultimo_numero = numero_a_sumar + ultimo_numero
    numero_a_sumar = numero_a_sumar + 1


print("la suma de los primeros", n, "numeros es de : ",ultimo_numero)