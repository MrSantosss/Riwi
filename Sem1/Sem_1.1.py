total = 0
compra = []
while  True:
    prenda = input("Ingrese el nombre de la Prenda o ingrese OUT para Terminar la lista : " ).upper()
    if prenda == "OUT":break
    cantidad = int(input(f'Ingrese la  Cantidad de {prenda} : ') )
    if cantidad <= 0 : break  
    precio = int(input("Ingrese el precio de la Prenda : "))
    if precio <= 0 :  break
    total = total + precio * cantidad
    descuento = int(input("Ingrese el Desceunto a Aplicar : "))
    if descuento < 0 or descuento > 100 : break
    precioD =  total - (total * descuento / 100)
    carrito = (prenda,cantidad,precio,descuento,precioD,total)
    compra.append(carrito)
print (compra)

