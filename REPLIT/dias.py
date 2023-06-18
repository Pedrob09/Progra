día_1 = int(input())
mes_1 = int(input())
año_1 = int(input())
día_2 = int(input())
mes_2 = int(input())
año_2 = int(input())


if año_1 != año_2:
    print("Los años no coinciden.")
elif año_1 % 4 == 0 and año_1 % 100 != 0:
    año_1 = 366
    año_2 = 366
    if mes_1 > 2:
        dia_actual_1 = (((367*mes_1 - 362)/12) + día_1) - 2
    else:
        dia_actual_1 = (((367*mes_1 - 362)/12) + día_1) - 1
    if mes_2 > 2:
        dia_actual_2 = (((367*mes_2 - 362)/12) + día_2) - 2
    else:
        dia_actual_2 = (((367*mes_2 - 362)/12) + día_2) - 1
    print(round(dia_actual_2 - dia_actual_1))

else:
    año_1 = 365
    año_2 = 365
    if mes_1 > 2:
        dia_actual_1 = (((367*mes_1 - 362)/12) + día_1) - 1
    else:
        dia_actual_1 = ((367*mes_1 - 362)/12) + día_1
    if mes_2 > 2 and año_2 == 366:
        dia_actual_2 = (((367*mes_2 - 362)/12) + día_2) - 1
    else:
        dia_actual_2 = ((367*mes_2 - 362)/12) + día_2

    print(round(dia_actual_2 - dia_actual_1))
