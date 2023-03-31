angulo_a = int(input("ingresar el angulo a: "))
angulo_b = int(input("ingresar el angulo b: "))
angulo_c = int(input("ingresar el angulo c: "))

if angulo_a > 0 and angulo_b > 0 and angulo_c > 0 and angulo_a + angulo_b + angulo_c == 180:
    if angulo_a == angulo_b == angulo_c:
        print("el triangulo es equilátero")
    if angulo_a == angulo_b or angulo_a == angulo_c or angulo_b == angulo_c:
        print("el triangulo es isóceles")
    if angulo_a != angulo_b and angulo_b != angulo_c and angulo_a != angulo_c:
        print("el triangulo es escaleno")
else:
    print("favor ingresar valores correctos")
    print("olamundo")
