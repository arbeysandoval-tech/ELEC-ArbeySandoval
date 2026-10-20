# #HERENCIA
# class persona:
#     def __init__(self, nombre):
#         self.nombre=nombre

#     def saludar(self):
#         return "Hola, soy {self.nombre}"

# class estudiante(persona):
#     pass

# estudiante1=estudiante("Ana")
# print(estudiante1.saludar()) # se llama la herencia

#super()
# class persona:
#     def __init__(self,nombre,edad,nota):
#         self.nombre = nombre
#         self.edad = edad
#         self.nota = nota

# class estudiante(persona):
#     def __init__(self,nombre,edad,carrera):
#         super().__init__(nombre,edad)
#         self.carrera = carrera
#         self.nota = nota

# estudiante1 = estudiante("camilo",22,"licenciado")
# print(estudiante1.nombre)
# print(estudiante1.edad)
# print(estudiante1.carrera)
# print(estudiante1.nota)

# class persona:
#      def __init__(self,nombre,edad,nota):
#          self.nombre = nombre
#          self.edad = edad
#          self.nota = nota
# class estudiante(persona):
#      def __init__(self,nombre,edad,carrera):
#          super().__init__(nombre,edad)
#          self.carrera = carrera
#          self.nota = nota
#          self.nota = nota

# estudiante1.presentarse()
# #METODO NUMERO 1 DE PERSONA
# estudiante1.mostrar_nota()
# # METODO NUMERO 2 DE  ESTUDIANTE
# estudiante1.mostrar_estado()
# #METODO NUMERO 3 DE ESTUDIANTE

# #SOBRESCRITURA DE METODOS
# class persona:
#     def presentarse(self):
#         return"soy una persona"

# class estudiante(persona):
#     def presentarse(self):
#         return"soy un estudiante"

# ENCAPSULAMIENTO

# class estudiante:
#     def __init__(self,nota):
#      self.nota=nota

#     def mostrar_nota(self):
#         return self.__nota

#_atributo uso por convencion para indicar que es privado y no se puede modificar
# __atributo acceso mas restringido python aplica name mangling
#regla rapida un guion bajo advierte  que dos guiones restringen mas

# class sensor:
#     def __init__(self):
#         self.ubicacion="sala"
#         self.temperatura=25
# #ubicacion es interno

# #getter y setter
# class estudiante:
#     def __init__(self,nota):
#         self.nota = nota

#     def mostrar_nota(self):
#         return self.nota 
    
#     def cambiar_nota(self,nueva_nota):
#         if 0 <= nueva_nota <= 5:
#             self.__nota = nueva_nota

# #validar antes de modificar 
# estudiante1= estudiante(4.5)
# print(estudiante1.mostrar_nota())
# estudiante1= estudiante(3.8)
# print(estudiante1.mostrar_nota())
# estudiante1= estudiante(7)
# print(estudiante1.mostrar_nota())


# def obtener_estado(self):
#     if self.__nota >= 3:
#         return f"aprobado con: {self.nota}"
#     else:
#         return f"reprobado con:{self.nota}"

# estudiante1= estudiante("luis",34,"lic. tecnologia",4.5)
# estudiante2= estudiante("pedro",25,"lic. tecnologia",2.8)

# print(estudiante1.obtener_estado())
# print(estudiante2.obtener_estado())

# class cuenta:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.__saldo = saldo
#     def consultar_saldo(self):
#         return self.__saldo
#     def depositar(self,cantidad):
#         if cantidad > 0:
#             self.__saldo += cantidad 

#ACTIVIDAD
class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        return f"mi nombre es {self.nombre} y actualmente tengo {self.edad} años"  
class estudiante(persona):
    def __init__(self,nombre,edad,carrera,nota):
        super().__init__(nombre,edad)
        self.carrera = carrera
        self.__nota = nota
    def mostrar_nota(self):
        return self.__nota
    def cambiar_nota(self,nueva_nota):
        if 0 <= nueva_nota <= 5:
            self.__nota = nueva_nota
    def obtener_estado(self):
        if self.__nota >= 3:
            return f"aprobado con: {self.__nota}"
        else:
            return f"reprobado con:{self.__nota}"
estudiante2 = estudiante("juan",25,"lic. informatica",2.4)
estudiante1 = estudiante("cristian", 20, "lic.tecnolgia", 4.5)
estudiante1.cambiar_nota(3.8)
estudiante2.cambiar_nota(7)
print(estudiante2.obtener_estado())
print(estudiante1.presentarse())
print(estudiante1.mostrar_nota())
print(estudiante1.obtener_estado())
print(estudiante2.presentarse())
print(estudiante2.mostrar_nota())
print(estudiante2.obtener_estado())

