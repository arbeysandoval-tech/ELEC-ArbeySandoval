# total= 0
# for vuelta in range(1, 6):
#     numero = int(input("Ingrese un número: "))
#     total = total + numero

# print("El total es:", total)

# for numero in range(1, 11):
#    if numero % 2 == 0:
#        print("El número", numero, "es par")
#        else:
#          print("El número", numero, "es impar")


# contador = 0
# suma = 0
# for numero in range(1, 11):
#     if numero % 2 == 0:
#         contador += 1
#         suma += numero
# print("Cantidad de pares:", contador)
# print("Suma de pares:", suma)

# for numero in range(1, 8):
#     if numero == 4:
#         break
#     print(numero)
# # 1, 2, 3

# texto = "Hola "
# for letra in texto:
#     print("letra:", letra)

#     texto ="area de texto"
#     texto = texto.lower()
#     if letra in "addskjhdhsk":
#         .....


# texto = "python"

# len(texto)    #6
# texto[0]      #p    
# texto[-1]     #n
# texto[0:3]    #pyt
# texto[::-1]   #nohtyp

# print(texto, 0, len(texto), texto[0], texto[-1], texto[0:3], texto[::-1])


# notas = [4, 5, 6, 7, 8, 9]
# print(notas[0])  #?
# print(notas[-1])  #?
# print(len(notas))  #?

# notas = [4.5,3.0,5.0]
# # for nota in notas:
# suma = 0
# for nota in notas:
#     suma += nota
# promedio = suma / len(notas)
# print("El promedio es:", promedio)

# notas = []
# for vuelta in range(3):
#     nota = float(input("Ingrese una nota: "))
#     notas.append(nota)
# print(notas)
    
# frutas = ["manzana", "pera", "uva",]

# frutas[1] = "mango"
# # ["manzana", "mango", "uva"]

# frutas.remove("uva")
# # elimina por valor
# eliminado = frutas.pop(0)
# # elimina por posición y devuelve el valor
# print(frutas)
# print("Fruta eliminada:", eliminado)


# numeros =[30, 10, 40, 20]
# numeros.sort() #modifica la lista 
# ordenado = sorted(numeros) #devuelve una nueva lista 
# numeros.reverse() #invierte la lista
# numeros.count(20) #cuenta coincidencias
# numeros.index(40) #primera posición donde aparece
# short_numeros = sorted(numeros, reverse=True) #ordena de mayor a menor
# print("Lista original:", numeros)
# print("Lista ordenada:", ordenado)
# sorted_numeros = sorted(numeros, reverse=True)
# reverse_numeros = list(reversed(numeros))
# print("Lista ordenada de mayor a menor:", sorted_numeros)
# print("Lista invertida:", reverse_numeros)

# nombres =["Ana", "luis","Carlos"]
# for i in range(len(nombres)):
#      print("estudiante" , i + 1, ":", nombres[i])

# notas =[2.5, 3.0, 4.0]
# for i in range(len(notas)):
#     if notas[i] < 3.0:
#         notas[i] = 3.0
# print(notas)

# estudiantes = [
#     ["Ana", 4,5],
#     #   0,  1
#     ["Luis", 3,8],
#     #   0,  1
#     ["Carlos", 4,2]
#     #   0,  1
# ]
# for estudiante in estudiantes:
#      print("estudiante:", estudiante[0], estudiante[1])

estudiantes = [
    ["Ana",[4,0, 3,5, 5,0]],
    ["Luis",[2,8, 3,0, 4,2]],
]
for estudiante in estudiantes:
    suma = 0
    for nota in estudiante[1]:
        suma += nota
        promedio = suma / len(estudiante[1])
        print(estudiante[0], round(promedio,2))

