#%%

import matplotlib.pyplot as plt
import pandas as pd

path= "JugadoresSeleccion.xlsx"
jugadores= pd.read_excel(path)
print(jugadores)

promedioEdad= sum(jugadores["EDAD"])/len(jugadores["EDAD"])
masChicos= jugadores[jugadores["EDAD"]<= promedioEdad]
masGrandes= jugadores[jugadores["EDAD"]>= promedioEdad]

#Seleccionamos las variables en los ejes cartesianos

xc = masChicos["NOMBRE"]
yc = masChicos["EDAD"]
xg = masGrandes["NOMBRE"]
yg = masGrandes["EDAD"]

#Genero el grafico que quiero y le agrego su descripcion

plt.axhline(y=promedioEdad, color='red', label="promedio")
plt.scatter(xc, yc, label="mas chicos")
plt.scatter(xg, yg, label="mas grandes")

#Configurar el espaciado entre los ticks
plt.xticks(rotation=60, ha="right")

plt.xlabel('jugadores')
plt.ylabel('Edad')

#muestro los label
plt.legend()
plt.show()

# %%
