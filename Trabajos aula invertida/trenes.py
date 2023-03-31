"""
Un tren parte desde la estación Los Domínicos en dirección hacia San Pablo, 
situada a 17.7 km de distancia, con una rapidez promedio de 60 km/h. 
Simultáneamente, otro tren parte en sentido contrario desde la estación San Pablo
con una rapidez media de 75 km/h.
¿A qué distancia de la estación Los Domínicos se cruzan ambos trenes
y a cuántos minutos de la partida?

desplazamiento = tiempo*velocidad
desplazamiento de ambos trenes = tiempo*(velocidad t.1 + velocidad t.2)
tiempo = d/(v.1+v.2)
tiempo en minutos = t*60
finalmente la distancia de desplazamiento desde los dominicos: 
d. = tiempo en minutos*velocidad tren 1
"""

distancia_entre_trenes = 17.7
velocidad_tren_1 = 60
velocidad_tren_2 = 75

tiempo = (distancia_entre_trenes/(velocidad_tren_1 + velocidad_tren_2))
tiempo_en_minutos = tiempo*60
distancia_desde_estacion_los_dominicos = tiempo*velocidad_tren_1
print("la distancia en la que se cruzan los trenes desde la estacion Los Dominicos es de:",
      distancia_desde_estacion_los_dominicos, "km", end="")
print(" y el tiempo en minutos que les tomó encontrarse es de:",
      tiempo_en_minutos, "minutos")
