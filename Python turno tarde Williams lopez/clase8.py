#%%
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.graph_objects as go

path= "ventas.xlsx"
pd.read_excel(path)

#%%

ventas = pd.read_excel(path,nrows=100)
zona = ventas.groupby(["Zona"]).agg(Conteo_pedidos=('Zona','count')).reset_index()
print(zona)

colores = ('Red','Purple','black','yellow')

plt.bar(zona["Zona"], zona["Conteo_pedidos"], color=colores)
plt.xlabel("Zona")
plt.ylabel("Conteo de productos")
plt.title("Conteo de productos por hora")
plt.xticks(rotation=20, ha="right")
plt.show() 

#Grafico de barras interactivo para conteo de productos por zona

fig = go.Figure(data=go.Bar(x=zona['Zona'], y=zona['Conteo_pedidos'], marker=dict(color=colores)))
fig.update_layout(title='Conteo de productos por zona', xaxis_title='Zona', yaxis_title='Conteo de productos')

fig.show()

ventas = pd.read_excel(path, usecols=["Tipo de producto"], nrows=100)
tipo_productos = ventas.groupby("Tipo de producto").agg(Conteo_Productos=('Tipo de producto','count')).reset_index()
print(tipo_productos)

plt.pie(tipo_productos['Conteo_productos'], labels=tipo_productos['Tipo de producto'], autopct='%1.1f%%')
plt.title('Ventas por Tipo de producto')

plt.show()
# %%
#Agregar y graficar por "Cerales" y "Cuidado personal"

ventas = pd.read_excel(path, usecols=("ID Cliente", "Tipo de producto", "País", "Zona"), nrows=100)
tipo_productos = ventas[ventas["Tipo de producto"].isin(["Cereales", "Cuidado personal"])]
tipo_productos = tipo_productos.groupby("Tipo de producto").agg(Conteo_Productos=('Tipo de producto', 'count')).reset_index()
print(tipo_productos)

plt.bar(tipo_productos["Tipo de producto"], tipo_productos["Conteo_productos"])
plt.xlabel("Tipo de producto")
plt.ylabel("Conteo de productos")
plt.title("Conteo de productos por tipo")
plt.show()
# %%
