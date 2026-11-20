import pandas as pd
import matplotlib.pyplot as plt

tabla=pd.read_csv("Distancia.csv")

plt.plot(tabla["Medicion"], tabla["Distancia"])
plt.bar(tabla["Medicion"], tabla["Distancia"])
plt.xlabel("Medicion")
plt.ylabel("Distancia")
plt.title("distancias medias por el HC-SR04")

plt.show()
