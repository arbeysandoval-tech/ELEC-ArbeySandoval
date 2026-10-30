# punto 1
productos=[]

# mayor_valor=[]
# # for i in range(4):
# #     nombre = input("Nombre: ")
# #     cantidad = int(input("Cantidad: "))
# #     valor_unitario = float(input("Valor unitario: "))
    
# #     equipos.append([nombre, cantidad, valor_unitario])

# # with open("equipos.txt", "w") as archivo:
# #     for equipo in equipos:
# #          archivo.write(f"{equipo[0]},{equipo[1]},{equipo[2]}\n")

for  i in range(3):
    nombre = input("Nombre: ")
    cantidad = int(input("Cantidad: "))
    valor_unitario = float(input("Valor unitario: "))
    
    productos.append([nombre, cantidad, valor_unitario])

with open ("productos.txt","w") as archivo:
    for producto in productos:
        archivo.writhe(f"{producto[0]},{producto[1]},{producto[2]}")

print("\ndatos guardados.txt")
with open ("productos.txt","r") as archivo:
    print("\nvalor_unitario")
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        cantidad = int(datos[1])
        valor_unitario = float(datos[2])

        valor_total = cantidad * valor_unitario
        valor_total += valor_total

print(nombre,".",cantidad,"x",valor_unitario,"=",valor_total)
if valor_total > 200000:
    mayor_valor.append([nombre,valor_total])

print("\nproductos con valor superior a 200000")
for productos in mayor_valor:
    print(producto[0],",",producto[2])

print("\nvalor de todos los productos:",valor_total)

# punto 2
        
class dispositivo:
    def __init__(self, nombre,marca,precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def mostrar(self):
        print("nombre:",self.nombre)
        print("marca:",self.marca)
        print("precio:",self.precio)
    def descuento(self,porcentaje):
        return self.precio * porcentaje

class sensor(dispositivo):
    def __init__(self,nombre,marca,precio,tipo,unidad,estado):
        super(). __init__(nombre,marca,precio)
        self.tipo = tipo
        self.__estado = estado
        self.unidad = unidad 

    def cambiar_estado(self,nuevo_estado):
        if nuevo_estado == "ACTIVO" or nuevo_estado == "INACTIVO":
            self.__estado = nuevo_estado
            return True
        else:
            return False
    def consular_estado(self):
        return self.__estado

    def mostrar(self):
        self. mostrar 
        print("TEMPERATURA:",self.temperatura, "C°")
        print("estado:",self.__estado())
    def mas_de_100_C(self):
        return self.temperatura > 100
    
sensor1 = sensor("sensoruno","arduino",200000,180,"INICATIVO")
sensor2 = sensor("sensorwill","sram",350000,100,"ACTIVO")

print("\nsensor 1")
sensor1.mostrar()
print("la temperatura es elevada",sensor1.mas_de_100_C())

print("\nsensor 2")
sensor2.mostrar()
print("la temperatura es adecuada",sensor2.mas_de_100_C())

print("\nCAMBIO DE ESTADO")
sensor1.cambiar_estado("INACTIVO")
print("Estado actual:",sensor1.cambiar_estado())


print("\n NO VALIDO")
if sensor1.cambiar_estado("limite superado"())
    print("Estado cambiado")
else:
    print("Estado no valido. No se cambio.")
print("Estado actual:",sensor11.consultar_estado())

print("\nDESCUENTO")
precio_final = sensor2.calcular_descuento(0.10)
print("Precio original:", sensor2.precio)
print("Precio con descuento:", precio_final)





    


       
        
    