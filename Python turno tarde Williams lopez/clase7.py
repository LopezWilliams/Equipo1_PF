

#%%
import pandas as pd

path= "JugadoresSeleccion.xlsx"
pd.read_excel(path)


# %%
path= "JugadoresSeleccion.xlsx"
jugadores=pd.read_excel(path)

print(jugadores["NOMBRE"])

#Vamos a buscar la info de Lionel

jugadores_lionel = jugadores[jugadores["NOMBRE"].str.contains("Lionel")]
print(jugadores_lionel)

#%%
#Vamos a buscar ahora por una edad en particular

jugadores_edad= jugadores[jugadores["EDAD"] == 25]
print(jugadores_edad)
# %%
promedioEdad= sum(jugadores["EDAD"])/len(jugadores["EDAD"])
masChicos= jugadores[jugadores["EDAD"]<= promedioEdad]
masGrandes= jugadores[jugadores["EDAD"]>= promedioEdad]

#Esto va a imprimir las edades sin decimales

print("el promdio de edad de los jugadores es ", round(promedioEdad))

print()
print(f'las mas chicos son')
print(masChicos)
print()
print(f'las mas grandes son')
print(masGrandes)








# %%
