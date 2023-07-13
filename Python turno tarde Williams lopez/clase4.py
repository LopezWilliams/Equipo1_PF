#librerias
#librerias de matematica
import math 

def seno(x): 
    resultado = math.sin(x) 
    return resultado 

print(round(seno(15))) 

#import math
from math import *

def seno(x):
    resultado = sin(x) 
    return resultado 

#funcion import datetime 

from datetime import datetime as dt

def fecha():
    dia = dt.now().day
    mes = dt.now().month
    año = dt.now().year 
    print(dia, mes, año) 

fecha()

#import random 

import random 

print(random.randrange(0,100)) 

lista = [] 

for i in range(10):
    lista.append(random.randint(0,100)) 

print(lista)
print(random.choice(lista))


