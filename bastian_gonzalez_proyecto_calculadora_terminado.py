lista = []
dicc = {}
while True:

    print("\t.:Calcula tus Ejercicios Tipo PDT:.")
    print("1. Numeros")
    print("2. Potencias")
    print("3. Funciones")

    usuario = int(
        input("ingresa la opcion del tipo de ejercicio que quieras calcular: "))

    if usuario == 1:
        operacion = input(
            "Ingresa la operacion con la cual quieras calcular los ejercicios(ojo poner solo iniciales, ejemplo, suma se escribe s, etc): ")
        if operacion.lower() == "s":  # esto creo que es innecesario si todas las operaciones son iguales
            a = float(input("ingresa un numero: "))
            b = float(input("ingresa otro numero: "))
            suma = a + b
            print("el resultado es", suma)
           # lista.append(suma)
        elif operacion.lower() == "m":
            a = int(input("Ingrese un numero: "))
            b = int(input("Ingrese otro numero: "))
            multiplicacion = a * b
            print("El producto de la multiplicacion es", multiplicacion)
            print(
                "recuerda que el producto entre un racional e irracional, siempre dara irracional")
            print("Recuerda que la multiplicacion de fracciones se hace hacia el lado, es decir, numerador con numerador, y denominador con denominador")
            print("OJO aca tambien con los signos, recuerda que la multiplicacion de signos iguales siempre da como resultado un numero positivo. Ejemplo -2*-4 = 8. Y para signos distintos, el resultado queda siempre negativo. Ejemplo -4*2 = 8")

        elif operacion.lower() == "d":
            a = int(input("Ingrese un numero: "))
            b = int(input("Ingrese otro numero: "))
            division = a / b
            print("El cociente de la division es", division)
            # a**1/2
            print("Recuerda que la division entre racional e irracional da siempre como resultado un numero irracional")
            print("Para dividir entre fracciones, solo tienes que multiplicar cruzado, pero OJO numerador con denominador te da como resultado numerador, y denominador con numerador te da como resultado denominador")
            print("Cuidado con los signos, recuerda que aca tienes que dividir los signos, pero es la misma logica que en la multiplicacion. Ejemplo 15:-3 = -5")

        elif operacion.lower() == "r":
            a = int(input("Ingrese un numero: "))
            b = int(input("Ingrese otro numero: "))
            resta = a - b
            print("el resultado es", resta)
            print("Ojo aqui con los signos tambien, recuerda que cuando hay una resta de enteros, o racionales, SIEMPRE se conserva el signo del numero mayor. Ejemplo 2-3.14 = -5.14")

    if usuario == 2:
        print("1. Calcular potencia simple")
        print(
            "2. Calcular multiplicacion de potencias de igual base con distinto exponente")
        print("3. Calcular division de potencias de igual base con distinto exponente")
        print("4. Calcular division de potencias de distinca base e igual exponente")
        print(
            "5. Calcular multiplicacion de potencias de distinta base y exponentes iguales")
        print("6. Calcular potencia de una potencia")

        operacion2 = int(input("ingresa una opcion: "))
        if operacion2 == 1:
            a = int(input("ingresa la base: "))
            b = int(input("ingresa el exponente: "))
            potencia = a**b
            print("El resultado de la potencia es", potencia,
                  "recuerda que todo numero elevado a 0 da como resultado 1")

        elif operacion2 == 2:
            a = int(input("ingresa la base de la primera potencia: "))
            b = int(input("ingresa el exponente de la primera potencia: "))
            c = int(input("ingresa la base de la segunda potencia: "))
            d = int(input("ingresa el exponente de la segunda potencia: "))
            if a == c:
                sumaexp = b + d
                print("se conserva la base", a or c)
                print("se suman los exponentes", b, "+", d, "=", sumaexp)

        elif operacion2 == 3:
            a = int(input("ingresa la base de la primera potencia: "))
            b = int(input("ingresa el exponente de la primera potencia: "))
            c = int(input("ingresa la base de la segunda potencia: "))
            d = int(input("ingresa el exponente de la segunda potencia: "))
            if a == c:
                restaexp = b - d
                print("se conserva la base", a or c)
                print("se restan los exponentes", b, "-", d, "=", restaexp)

        elif operacion2 == 4:
            a = int(input("ingresa la base de la primera potencia: "))
            b = int(input("ingresa el exponente de la primera potencia: "))
            c = int(input("ingresa la base de la segunda potencia: "))
            d = int(input("ingresa el exponente de la segunda potencia: "))
            if b == d:
                divbase = a/b
                print("se conservan los exponentes", b or d)
                print("se dividen las bases", a, ":", c, "=", divbase)

        elif operacion2 == 5:
            a = int(input("ingresa la base de la primera potencia: "))
            b = int(input("ingresa el exponente de la primera potencia: "))
            c = int(input("ingresa la base de la segunda potencia: "))
            d = int(input("ingresa el exponente de la segunda potencia: "))
            if b == d:
                multbase = a*c
                print("se conservan los exponentes", b or d)
                print("se multiplican las bases", a, "*", c, "=", multbase)

        elif operacion2 == 6:
            a = int(input("ingresa la base: "))
            b = int(input("ingresa el primer exponente: "))
            c = int(input("ingresa el segundo exponente: "))
            potenciapot = (a)**(b*c)
            print("El resultado es", potenciapot)

    if usuario == 3:
        print("1. Calcular una funcion lineal")
        # Solucion1 -b-(b**2-4*a*c)**1/2 resultado = solucion1 /2a
        print("2. Calcular una funcion cuadratica")

        # solucion2 -b+(b**2-4*a*C)**1/2 resultado2 = solucion2 /2a
        operacion3 = int(input("ingresa una opcion: "))

        if operacion3 == 1:
            a = int(input("ingresa el numero que acompaña a ", "x",
                    "(recuerda que el numero que acompaña a x se llama pendiente: "))  # esta es la pendiente
            b = int(input("ingresa el segundo numero (si la funcion no posee una valor de b, coloca 0 aca)recuerda que si hay un valor distinto de 0, esto pasa a ser una funcion afin, y esta parte se llama coeficiente de posicion: "))
            if b == 0:
                for i in range(-5, 5):
                    dicc[i] = a*i

                print(dicc)

            else:
                for i in range(-5, 5):
                    dicc[i] = a*i+b

                print(dicc)

        elif operacion3 == 2:
            a = int(input("ingresa el valor que acompaña a x^2: "))
            b = int(input("ingresa el valor que acompaña a x sin elevar: "))
            c = int(
                input("ingresa el termino libre (si es que c no existe, coloca un 0): "))
            discriminante = (b**2-4*a*c)
            if discriminante == 0:
                solucion1 = (-b-(b**2-4*a*c)**1/2) / 2*a
                solucion2 = (-b+(b**2-4*a*c)**1/2) / 2*a
                print(solucion1)
                print(solucion2)
                print("la funcion tiene dos soluciones reales e iguales")
            elif discriminante > 0:
                solucion1 = (-b-(b**2-4*a*c)**1/2) / 2*a
                solucion2 = (-b+(b**2-4*a*c)**1/2) / 2*a
                print(solucion1)
                print(solucion2)
                print("la funcion tiene dos soluciones reales y distintas")

            elif discriminante < 0:
                print("la funcion no tiene soluciones reales")
