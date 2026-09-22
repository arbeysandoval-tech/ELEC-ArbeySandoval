# def presentrar(nombre,edad):
#     print("nombre:",nombre)
#     print("edad:",edad)

#     presentar("laura",22)

# def sumar(a,b):
#     print (a+b)
# resultado=sumar(5,3)
# print(resultado)

# def sumar(a,b):
#     return (a+b)
# resultado=sumar(5,3)
# print(resultado)

# def multiplicar(a,b):
#     return a*b
# resultado=multiplicar(4,5)+10

# print(resultado)

# def calcular_promedio(notas):
#     suma=0
#     for nota in notas:
#         suma +=nota
#     return suma/len(notas)
# notas_ana=[4.0,3.5,5.0]
# promedio=calcular_promedio(notas_ana)   
# print(round(promedio,2))

# def calcular():
#     resultado=20
#     print(resultado)
# calcular()
# print(resultado)

# nombre="laura"
# def saludar(): 
#         print(nombre)
# saludar()

# contador=10
# def aumentar():
#     contador=contador+1
#     print(contador)
# aumentar()  //aumentar suma

# def aumentar(numero):
#     return numero+1 //retorno
# contador= 10
# contador=aumentar(contador)
# print(contador)

## EJERCICIO EN CLASE
# def calcular_total(precio,cantidad): ##parametros  dentro de la funcion
#     return precio *cantidad

# producto={
#  "nombre":"teclado",
#  "precio":80000,
#  "cantidad":3
# }

# producto["total"]= calcular_total(
#     producto["precio"],
#     producto["cantidad"]  
# )
# print(producto)

# puntos = 5

# def calcular_puntos():
#     puntos=puntos+10
#     print(puntos)

# sumar_puntos()

# def sumar_puntos(puntos):
#    return puntos+10

# puntos=5
# puntos=sumar_puntos(puntos)
# print(puntos)

## TALLER EN CLASE
def calcular_promedio(notas):
    suma=0
    for nota in notas:
        suma +=nota
    return suma/len(notas)  
estudiantes=[
    {"nombre":"Ana","notas":[4.0,3.5,5.0]},
    {"nombre":"Luis","notas":[2.5,3.0,5.0]},
    {"nombre":"carlos","notas":[4.5,4.0,4.8]},
]
for estudiante in estudiantes:
    promedio=calcular_promedio(estudiante["notas"])
    if promedio>3.0:
        estado="aprobado"
    else:
        estado="no aprobado"
    
    estudiante["peomedio"]=round(promedio,2)
    estudiante["estado"]=estado
print(estudiantes)

    
    

    

        


