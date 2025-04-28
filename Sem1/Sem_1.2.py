
producto = input ("Ingrese el Nombre del Producto")
precioU = int(input("Ingrese el Valor unitario del producto "))
if precioU <= 0 :
    print("Valor por unidad no Valido")
else :
    cantidad = int(input("Ingrese la Cantidad de unidades ")) 
    Total = precioU * cantidad
    if cantidad <= 0 :
        print("Unidades no Validas")
    else :
        descuento = int(input("Ingrese la Cantidad del Descuento si Aplica"))
        precio =  Total - (Total * descuento / 100)
        if descuento < 0 or descuento > 100 :
            print("Valor de el Descuento No Valido")
        else:
            print ("     COMPRA      ")
            print ("Producto : ", producto)
            print ("Unidades Compradas : ",cantidad)
            print ("Valor De la compra Con el Descuento Aplicado : ", precio)
            print ("Valor Originial de la compra : ", Total)
    