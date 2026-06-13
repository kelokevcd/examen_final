import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
datos = pd.read_csv("living (6) (3).csv", encoding="latin1")
print(datos.info())
print(datos.head(20))
nuevo = pd.DataFrame(datos) 
nuevo.replace(np.nan, "0", inplace=True)
print(nuevo.describe())
num_filas = len(nuevo)
num_columnas = len(nuevo.columns)
costo_promedio = nuevo["Cost of living, 2017"].mean()
nuevo_ordenado_alto = nuevo.sort_values(by="Cost of living, 2017", ascending=False)
pais_mas_alto = nuevo_ordenado_alto["Countries"].head(1).values[0]
nuevo_ordenado_bajo = nuevo.sort_values(by="Cost of living, 2017", ascending=True)
pais_mas_bajo = nuevo_ordenado_bajo["Countries"].head(1).values[0]
datos_peru = nuevo[nuevo["Countries"] == "Peru"]
costo_peru = datos_peru["Cost of living, 2017"].values[0]
ranking_peru = datos_peru["Global rank"].values[0]
print("1. Revisión inicial del dataset")
print("Nro. de Filas:", num_filas)
print("Nro. de Columnas:", num_columnas)
print("Costo de vida promedio:", costo_promedio)
print("País con costo de vida más alto:", pais_mas_alto)
print("País con costo de vida más bajo:", pais_mas_bajo)
print("Costo de Vida en Perú:", costo_peru)
print("Ranking de Perú:", ranking_peru)
print("------------------------------")

# 2. Desarrollar visualizaciones

# Los 10 países con el costo de vida más alto
top_10_altos = nuevo.sort_values(by="Cost of living, 2017", ascending=False).head(10)
plt.bar(top_10_altos["Countries"], top_10_altos["Cost of living, 2017"])
plt.title("Los 10 países con el costo de vida más alto")
plt.xticks(rotation=45)
plt.show()

# Los 10 países con el costo de vida más bajo
top_10_bajos = nuevo.sort_values(by="Cost of living, 2017", ascending=True).head(10)
plt.bar(top_10_bajos["Countries"], top_10_bajos["Cost of living, 2017"])
plt.title("Los 10 países con el costo de vida más bajo")
plt.xticks(rotation=45)
plt.show()

# El costo de vida de los países de América
paises_america = nuevo[nuevo["Continent"] == "America"]
plt.bar(paises_america["Countries"], paises_america["Cost of living, 2017"])
plt.title("Costo de vida de los países de América")
plt.xticks(rotation=90)
plt.show()
