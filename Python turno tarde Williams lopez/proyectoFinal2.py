#%% 
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.graph_objects as go 

path= "datos-ciberdelitos2022.xlsx"
pd.read_excel(path)


DivisionGenero = pd.read_excel(path,nrows=500)
Sexo = DivisionGenero.groupby(["Sexo"]).agg(Conteo=('Sexo','count')).reset_index()
print(Sexo)

colores = ('Red','Purple','black','yellow')

plt.bar(Sexo["Sexo"], Sexo["Conteo"], color=colores)
plt.xlabel("División por Género")
plt.ylabel("Cantidad")
plt.title("Espectro de Participacion por Genero")
plt.xticks(rotation=0, ha="right")
plt.show() 

#Grafico de barras interactivo 

fig = go.Figure(data=go.Bar(x=Sexo['Sexo'], y=Sexo['Conteo'], marker=dict(color=colores)))
fig.update_layout(title='Espectro de Participación por Género', xaxis_title='Sexo', yaxis_title='Cantidad')

fig.show()

DivisiónGenero = pd.read_excel(path, usecols=["Sexo"], nrows=100)
Sexo = DivisionGenero.groupby("Sexo").agg(Conteo_Genero=('M','F','count')).reset_index()
print(Sexo)

plt.pie(Sexo['Conteo_diariamente'], labels= DivisionGenero['M','F'], autopct='%1.1f%%')
plt.title('Espectro de Participación por Género')

plt.show()
# %%


plt.bar(Sexo["Uso de Redes"], Sexo["Conteo_genero"])
plt.xlabel("Division por Genero")
plt.ylabel("Cantidad")
plt.title("Espectro de Participación por Genéro")
plt.show()

