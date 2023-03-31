# ENTRADA
import math
print()
Cateto_a = float(input("Favor ingresar el lado del cateto a:"))
Cateto_b = float(input("Favor ingresar el lado del cateto b:"))
# PROCESAMIENTO
if Cateto_a > 0 and Cateto_b > 0:
    Hipotenusa = math.sqrt(Cateto_a ** 2 + Cateto_b ** 2)
# SALIDA
    print("El valor de la hipotenusa es:", Hipotenusa)

else:
    print("ingresar valor de catetos correctos")