# Pedir la cantidad de piezas
cantidad_piezas = int(input("Ingrese la cantidad de piezas: "))

# Crear una matriz vacía para representar el tablero
tablero = [["__" for _ in range(8)] for _ in range(8)]

# Pedir las piezas una por una
for _ in range(cantidad_piezas):
    nombre_pieza = input("Ingrese el nombre de la pieza: ")
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    
    # Colocar la pieza en las coordenadas especificadas en el tablero
    tablero[8 - fila][columna - 1] = nombre_pieza

# Mostrar el tablero con las piezas
for fila in tablero:
    print(" ".join(fila))

    
