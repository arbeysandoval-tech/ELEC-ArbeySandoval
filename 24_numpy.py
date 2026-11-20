import numpy as np 

# temperaturas = np.array([26, 28, 31, 29, 35,33,27]) 

# temp_aumentadas=temperaturas + 2
# promedio_temp=np.mean(temperaturas)
# temp_max=np.max(temperaturas)
# temp_min=np.min(temperaturas)


# print(temp_aumentadas)
# print(promedio_temp)
# print(temp_max)
# print(temp_min)
# print(temperaturas[0])
# print(temperaturas[6])
# temp_bajas=temperaturas[temperaturas<28]
# print(temp_bajas)
# temp_altas=temperaturas[temperaturas>29]
# print(temp_altas)

temperaturas =np.array([20,21,19,22,20,21,19])
suma_temperaturas=np.sum(temperaturas)
promedio_temperaturas=np.mean(temperaturas)
media_std=np.std(temperaturas)
print(suma)
print(round(promedio_temperaturas,2))
print(round(media_std,2))
