# %%
import pandas as pd 

serie = pd.Series([1,2,3,4,5,6,7,8,9])

print(serie) 

cantidad_elementos = serie.count() 

print("La cantidad de elementos que hay es" , cantidad_elementos)

# %%
#dataframes

df = pd.DataFrame([[1,1,1,1,1],
                   [2,2,2,2,2],
                   [1,2,6,5,9]])
print(f'la suma del DF es: \n\ {df.sum()}')

# %%
df_nombres= pd.DataFrame()
df_nombres['nombres'] = ['Williams','Arani','Camila']


df_nombres['edad'] = [18,18,17]

# %%
def sumar_uno(x):
    return x + 1
df_nombres['edad'].apply(sumar_uno)
# %%
