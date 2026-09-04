# Punto 1A
# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#     print("mayor de edad")
# else:
#     print("menor de edad")
# el problema era que no estaba convirtiendo la edad a entero por lo tanto la comparación no funcionaba el codigo.

#Punto 1B
# Nota = float(input("Ingrese su nota: "))
# if Nota < 5.0 and Nota >= 4.5:
#     print("Desempeño superior")
# elif Nota < 4.5 and Nota >= 3.0:
#     print("aprobado")
# elif Nota < 3.0:
#     print("no aprobado")

#Punto 2

# ingrrese_su_nota = float(input("Ingrese su nota: "))
# nota_invalid = ingrrese_su_nota < 0 or ingrrese_su_nota > 5
# if nota_invalid:
#     print("Nota invalida")
#     menor = ingrrese_su_nota < 3.0
#     if menor:
#         print("No aprobado")
# elif ingrrese_su_nota >= 3.0 and ingrrese_su_nota < 4.0:
#     print("desempeño basico")
# elif ingrrese_su_nota >= 4.0 and ingrrese_su_nota < 4.6:
#     print("desempeño alto")
# elif ingrrese_su_nota >= 4.6 and ingrrese_su_nota <= 5.0:
#     print("desempeño superior")
    
#punto 3
total_ventas = 0
cantidad_ventas = 0
opcion = 0
while opcion != 3:
    print("1. registrar venta")
    print("2. consultar resumen")
    print("3. finalizar")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        venta = float(input("cantidad: "))
        total_ventas += venta
        cantidad_ventas += 1
    elif opcion == 2:
        if cantidad_ventas > 0:
            resumen = f"Total de ventas: {total_ventas}, Cantidad de ventas: {cantidad_ventas}"
            promedio = total_ventas / cantidad_ventas
            print(resumen)
        else:
            print("No se han registrado ventas.")
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Intente nuevamente.")


