#%% 
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.graph_objects as go 

path= "datos-ciberdelitos2022.xlsx"
pd.read_excel(path)

#%%

UsodeRS = pd.read_excel(path,nrows=500)
Frecuencia = UsodeRS.groupby(["Frecuencia"]).agg(Conteo=('Frecuencia','count')).reset_index()
print(Frecuencia)

colores = ('Red','Purple','black','yellow')

plt.bar(Frecuencia["Frecuencia"], Frecuencia["Conteo"], color=colores)
plt.xlabel("Frecuencia")
plt.ylabel("Respuestas")
plt.title("Regularidad de Uso de Redes Sociales")
plt.xticks(rotation=60, ha="right")
plt.show() 

#Grafico de barras interactivo 

fig = go.Figure(data=go.Bar(x=Frecuencia['Frecuencia'], y=Frecuencia['Conteo'], marker=dict(color=colores)))
fig.update_layout(title='Regularidad de Uso de Redes sociales', xaxis_title='Frecuencia', yaxis_title='Uso de Redes')

fig.show()

UsodeRS = pd.read_excel(path, usecols=["Frecuencia"], nrows=100)
Frecuencia = UsodeRS.groupby("Frecuencia").agg(Conteo_Diariamente=('Diariamente','count')).reset_index()
print(Frecuencia)

plt.pie(Frecuencia['Conteo_diariamente'], labels= UsodeRS['Diariamente'], autopct='%1.1f%%')
plt.title('Uso diario de Redes')

plt.show()
# %%


plt.bar(Frecuencia["Uso de Redes"], Frecuencia["Conteo_diario"])
plt.xlabel("Frecuencia")
plt.ylabel("Regularidad")
plt.title("Usos de Redes Sociales")
plt.show()
# %%
