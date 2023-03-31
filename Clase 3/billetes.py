billete_20000 = 20000
billete_10000 = 10000
billete_5000 = 5000
billete_2000 = 2000
billete_1000 = 1000
moneda_500 = 500
moneda_100 = 100
moneda_50 = 50
moneda_10 = 10
moneda_5 = 5
moneda_1 = 1
n_billete_20000 = 0
n_billete_10000 = 0
n_billete_5000 = 0
n_billete_2000 = 0
n_billete_1000 = 0
n_moneda_500 = 0
n_moneda_100 = 0
n_moneda_50 = 0
n_moneda_10 = 0
n_moneda_5 = 0
n_moneda_1 = 0
# ENTRADA
Cantidad_dinero = float(input("Favor ingresar la cantidad de dinero que desea desglosar: "))
# PROCESAMIENTO
if Cantidad_dinero >= billete_20000:
    n_billete_20000 = int(Cantidad_dinero / billete_20000)
    Cantidad_dinero = Cantidad_dinero % billete_20000
if Cantidad_dinero >= billete_10000:
    n_billete_10000 = int(Cantidad_dinero / billete_10000)
    Cantidad_dinero = Cantidad_dinero % billete_10000
if Cantidad_dinero >= billete_5000:
    n_billete_5000 = int(Cantidad_dinero / billete_5000)
    Cantidad_dinero = Cantidad_dinero % billete_5000
if Cantidad_dinero >= billete_2000:
    n_billete_2000 = int(Cantidad_dinero / billete_2000)
    Cantidad_dinero = Cantidad_dinero % billete_2000
if Cantidad_dinero >= billete_1000:
    n_billete_1000 = int(Cantidad_dinero / billete_1000)
    Cantidad_dinero = Cantidad_dinero % billete_1000
if Cantidad_dinero >= moneda_500:
    n_moneda_500 = int(Cantidad_dinero / moneda_500)
    Cantidad_dinero = Cantidad_dinero % moneda_500
if Cantidad_dinero >= moneda_100:
    n_moneda_100 = int(Cantidad_dinero / moneda_100)
    Cantidad_dinero = Cantidad_dinero % moneda_100
if Cantidad_dinero >= moneda_50:
    n_moneda_50 = int(Cantidad_dinero / moneda_50)
    Cantidad_dinero = Cantidad_dinero % moneda_50
if Cantidad_dinero >= moneda_10:
    n_moneda_10 = int(Cantidad_dinero / moneda_10)
    Cantidad_dinero = Cantidad_dinero % moneda_10
if Cantidad_dinero >= moneda_5:
    n_moneda_5 = int(Cantidad_dinero / moneda_5)
    Cantidad_dinero = Cantidad_dinero % moneda_5
if Cantidad_dinero >= moneda_1:
    n_moneda_1 = int(Cantidad_dinero / moneda_1)
    Cantidad_dinero = Cantidad_dinero % moneda_1
# SALIDA
if n_billete_20000 > 0:
    print("La cantidad de billetes de $20.000 es:", n_billete_20000)
if n_billete_10000 > 0:
    print("La cantidad de billetes de $10.000 es:", n_billete_10000)
if n_billete_5000 > 0:
    print("La cantidad de billetes de $5.000 es:", n_billete_5000)
if n_billete_2000 > 0:
    print("La cantidad de billetes de $2.000 es:", n_billete_2000)
if n_billete_1000 > 0:
    print("La cantidad de billetes de $1.000 es:", n_billete_1000)
if n_moneda_500 > 0:
    print("La cantidad de monedas de $500 es:", n_moneda_500)
if n_moneda_100 > 0:
    print("La cantidad de monedas de $100 es:", n_moneda_100)
if n_moneda_50 > 0:
    print("La cantidad de monedas de $50 es:", n_moneda_50)
if n_moneda_10 > 0:
    print("La cantidad de monedas de $10 es:", n_moneda_10)
if n_moneda_5 > 0:
    print("La cantidad de monedas de $5 es:", n_moneda_5)
if n_moneda_1 > 0:
    print("La cantidad de monedas de $1 es:", n_moneda_1)