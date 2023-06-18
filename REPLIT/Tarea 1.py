# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA/FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: 0-G-1
# PROFESOR DE TEORÍA: ANDRES RICE
# PROFESOR DE LABORATORIO: FELIPE REYES
#
# AUTOR
# NOMBRE: Pedro Alejandro Berrios Peréz
# RUT: 21.412.626-5
# CARRERA: Ingeniería En Ejecucion Electrica
# <Separamos el problema general en partes para hacerlo de manera eficiente pra hacer el input de todos los productos de manera que queden en listas, luego de esto se calcula la boleta total con y sin impuesto, se calculan los casos de productos como vinos, bebidas alcohólicas, etc. Siguendo a esto se hacen los inputs de los descuento que escribe el cajero>


# Ingreso de elementos en forma de strings separado por comas (nombre,tipo,precio,cantidad)
flag = True
prod = []
fallos = []
cont = 1
while flag:
    i = input()
    B = i.split(",")
    if i != "FIN LECTURA":
        if len(B) != 4:
            fallos.append(cont)
            cont += 1
        elif int(B[3]) < 1 or int(B[2]) < 1:
            fallos.append(cont)
            cont += 1
        else:
            prod.append(B)
            cont += 1
    else:
        flag = False


# Calculo de la boleta total sin impuestos
total_simp = 0
for producto in prod:
    A = float(producto[2])*float(producto[3])
    total_simp += A


# Calculo de boleta con impuestos por productos
total_imp = 0
cat = ['vinos', 'cigarros', 'bebidas alcohólicas', 'cosas de furros']
for producto in prod:
    if producto[1] in cat:
        total_imp += (float(producto[2])*float(producto[3]))*1.25
    else:
        total_imp += (float(producto[2])*float(producto[3]))*1.20

# Creacion de descuentos
flag = True
desc = []
fallodesc = []
c = 1
while flag:
    d = input()
    K = d.split(",")
    if d != "FIN DESCUENTOS":
        if len(K) != 3:
            fallodesc.append(c)
            c += 1
        elif int(K[2]) < 0 or int(K[2]) > 99:
            fallodesc.append(c)
            c += 1
        else:
            desc.append(K)
            c += 1
    else:
        flag = False


# Aplicacion de los descuentos a los productos y al total de la boleta.
xdesc = []
tdesc = 0
for descuentos in desc:
    temp = []
    for productos in prod:
        temp = []
        if descuentos[1] == productos[1]:
            if producto[1] in cat:
                dtotal = float(productos[2])*float(productos[3])*float(descuentos[2])/100*1.25
                tdesc += dtotal
                temp.append(descuentos[1])
                temp.append(dtotal)
            else:
                dtotal = float(productos[2])*float(productos[3])*float(descuentos[2])/100*1.20
                tdesc += dtotal
                temp.append(descuentos[1])
                temp.append(dtotal)
            xdesc.append(temp)


# Calculo del valor real de la boleta final.
valor_total = total_imp - tdesc
nuevo_vtotal = valor_total
for descuentos_total in desc:
    temp = []
    if descuentos_total[0] == "al total":
        dtotal2 = nuevo_vtotal * float(descuentos_total[2])/100
        nuevo_vtotal = nuevo_vtotal - dtotal2
        temp.append(descuentos_total[1])
        temp.append(dtotal2)
        xdesc.append(temp)


# Print de fallos en ingresos por pantalla, al final de la ejecucion.
for num in fallos:
    print('Error de ingreso en producto:', num)
for num in fallodesc:
    print('Error de ingreso en descuento:', num)

# Eliminacion y suma de descuentos


def sumar_valores(lista):
    suma_por_valor = {}

    for item in lista:
        valor_str = item[0]
        valor_int = item[1]

        if valor_str in suma_por_valor:
            suma_por_valor[valor_str] += valor_int
        else:
            suma_por_valor[valor_str] = valor_int

    return suma_por_valor


resultado = sumar_valores(xdesc)


for clave, valor in resultado.items():
    print("Con el descuento '%s', te ahorraste $%s" % (clave, valor))

print('El total de su boleta es de ${},'.format(
    nuevo_vtotal), 'impuestos incluidos')
print('Esta compra acumula', round(nuevo_vtotal/100), 'oso puntos')
print('Gracias, vuelva prontos')



