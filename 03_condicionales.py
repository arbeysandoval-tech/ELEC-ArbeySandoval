#  usuario= input("usuario: ")   
#  nombre =input("nombre: ")
#  edad= input("edad: ")
#  temperaturacorporal=float(input("temperaturacorporal: "))
#  nota=float(input("NOTA DE 0.0 A 5.0 "))
#  carnet = input ("¿tiene carnet? si o no : ")

#  mayor_edad=edad>=18
#  temp_adecuada=temperaturacorporal==37.5
#  notafinal=nota>=0.0 and nota<=5.0
#  requisito=carnet=="si"
#  cumple_requisitos=mayor_edad and temp_adecuada and requisito

#  print ("cumple requisitos de ingreso ",    cumple_requisitos)
#  print ("es mayor de edad",   mayor_edad)
#  print("tiene carnet" ,requisito)
#  print("tiene temperatura normal",temp_adecuada )


# nota=float(input("Nota: "))
# if nota<0 or nota >5:
#   print("nota no valida")
# elif nota <3:
#      print ("insuficiente")
# elif nota<4.6:
#      print ("alto")


# edad =25
# matricula ="si"
# contraseña = "azul21"
# if edad < 18:
#     print("Acceso restringido")
# else:
#         if matricula == "si":
#             if contraseña == "azul21":
#                 print("Bienvenido")
#             else :
#                  print("Contraseña incorrecta")
#         else:
#                 print("No tiene matricula")
     
# Nombre = input("Nombre: ")
# Edad = int(input("Edad: "))
# tiene_invitacion = input("¿Tiene invitación? (si/no): ")
# invitacion= tiene_invitacion.lower() 
# if Edad >= 18 and tiene_invitacion == "si":
#      print("Autorizado ", Nombre)
# elif Edad <= 18:
#     print("acceso denegado, ", Nombre)
# else:
#         print("Necesita invitación, ", Nombre)

# numero = 1
# while numero <= 5:
#     print(numero)
#     numero += 1

# numero = 1
# while numero <= 3:
#     print(numero) # nunca se detiene el ciclo
    
# contraseña = "" 
# while contraseña != "phyton":
#     contraseña = input("contraseña: ")

# print("Bienvenido.") # nunca se detiene el ciclo/ while es ideal para un gran numero de intentos

contraseña = "" 
intentos = 0

# while contraseña != "phyton" and intentos < 3:
#     contraseña = input("contraseña: ")
#     intentos += 1

# if contraseña == "phyton":
#     print(" Acesso Autorizado")
# else:
#     print("Acceso bloquedo")

pin_correcto = "2580"
max_intentos = 3
intentos = 0
while intentos < max_intentos:
    pin_ingresado = input("Ingrese el PIN: ")
    if pin_ingresado == pin_correcto:
        print("Acceso autorizado")
        intentos +=1
    else:
        print("PIN incorrecto")
        intentos += 1