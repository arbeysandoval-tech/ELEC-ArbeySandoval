import pandas as pd
datos = {
    "Medicion": [1,2,3,4,5],
    "Distancia": [15,18,23,13,30]
}
tabla_datos = pd.DataFrame(datos)
# # print(total_datos)
# print(tabla_datos["Distancia"])
# prom_distancia = tabla_datos["Distancia"].mean()
# print(prom_distancia)
# dis_max = tabla_datos["Distancia"].max()
# print(dis_max)
temp_altas = tabla_datos[tabla_datos["Distancia"]>=20]
print(temp_altas)
tabla_datos["Distancia Doble"] = tabla_datos["Distancia"]*2
print(tabla_datos)

tabla_datos.to_csv("Distancia.csv", index=False)

