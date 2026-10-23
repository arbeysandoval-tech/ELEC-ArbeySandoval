# # #taller de archivos
# # #EJERCICIO 1
# # equipos=[]
# # valor_total=0
# mayor_valor=[]
# # for i in range(4):
# #     nombre = input("Nombre: ")
# #     cantidad = int(input("Cantidad: "))
# #     valor_unitario = float(input("Valor unitario: "))
    
# #     equipos.append([nombre, cantidad, valor_unitario])

# # with open("equipos.txt", "w") as archivo:
# #     for equipo in equipos:
# #          archivo.write(f"{equipo[0]},{equipo[1]},{equipo[2]}\n")
    
# print("\nDatos guardados.txt")
# with open("equipos.txt", "r") as archivo:
#     print("\nvalor_unitario")
#     for linea in archivo:
#         datos = linea.strip().split(",")
#         nombre = datos[0]
#         cantidad =int(datos[1])
#         valor_unitario = float(datos[2])
        
#         valor_total = cantidad * valor_unitario
#         valor_total += valor_total
        
#         print(nombre,".",cantidad,"x",valor_unitario,"=",valor_total)
#         if valor_total > 2000000:
#             mayor_valor.append([nombre,valor_total])
# print("\nequipos que valen mas de 2000000")
# for equipo in mayor_valor:
#     print(equipo[0],".",equipo[1])
# print("\nvalor de todos los equipos:",valor_total)

#EJERCICIO 2
 
class dispositivo:
    def __init__(self, nombre, marca,precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def mostrar(self):
        print("nombre:",self.nombre)
        print("marca:",self.marca)
        print("precio:",self.precio)
    def descuento(self,porcentaje):
        return self.precio * porcentaje

class portatil(dispositivo):
    def __init__(self,nombre,marca,precio,memoria_ram,estado):
        super(). __init__(nombre,marca,precio)
        self.memoria_ram = memoria_ram
        self.__estado = estado
       
        
    def cambiar_estado(self,nuevo_estado):
        if nuevo_estado == "Disponible" or nuevo_estado == "prestado":
            self.__estado = nuevo_estado
            return True
        else:
            return False
    def consular_estado(self):
        return self.__estado

    def mostrar(self):
        self. mostrar 
        print("memoria RAM:",self.memoria_ram,"GB")
        print("estado:",self.__estado())
    def mas_de_16gb(self):
        return self.memoria_ram > 16
    
portatil1 = portatil("portatil asus","asus",3000000,16,"Disponible")
portatil2 =portatil("portatil hp","hp",2500000,8,"prestado")

print("\ncomputador 1")
portatil1. mostrar()
print("tiene 16gb o mas memoria RAM",portatil1.mas_de_16gb())

print("\ncomputador 2")
portatil2. mostrar()
print("tiene 16gb o mas memoria RAM",portatil2.mas_de_16gb())

print("\nCAMBIO DE ESTADO")
portatil1.cambiar_estado("Prestado")
print("Estado actual:", portatil1.consultar_estado())


print("\n NO VALIDO")
if portatil1.cambiar_estado("En mantenimiento"):
    print("Estado cambiado")
else:
    print("Estado no valido. No se cambio.")
print("Estado actual:", portatil1.consultar_estado())


print("\nDESCUENTO")
precio_final = portatil2.calcular_descuento(0.10)
print("Precio original:", portatil2.precio)
print("Precio con descuento:", precio_final)







    

