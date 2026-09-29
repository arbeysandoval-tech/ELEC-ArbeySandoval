productos=[
    {"nombre":"teclado","precio":80000,"cantidad":3},
    {"nombre":"mouse","precio":50000,"cantidad":5},
    {"nombre":"monitor","precio":700000,"cantidad":2},
    {"nombre":"camara","precio":120000,"cantidad":1},
]
def calcular_total(precio,cantidad):
    return precio *cantidad
for producto in productos:
    total=calcular_total(producto["precio"],producto["cantidad"])
    producto["total"]= total#calcular_total(producto["precio"],producto["cantidad"])
    print(producto["nombre"], producto["total"])
valor_total_inventario=0
for producto in productos:
    valor_total_inventario += producto["total"]
print("valor total inventario=", valor_total_inventario)
bajo= 0
for producto in productos:
    if producto["cantidad"]<=2:
        bajo.append (producto["nombre"])
print("bajo stock=", bajo)

