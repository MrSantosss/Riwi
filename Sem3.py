#se define la lista que seria como tal el carrito de compra
carrito = []
#La funcion ingresar es aquel que pide los datos de aquel producto que desee añadir, cada vez que se invoque la funcion ingresar se crea un nuevo diccionario y los almacena todos en la lista carrito 
def ingresar (): 
    try:
     producto = {} 
     nombre = input(" Ingrese el Produto a Añadir : ").lower().strip()
     precio = float(input(" Ingrese el Precio unitario de el Producto : "))
     if precio < 0 :
         print (" Ingrese un Valor Positivo ")
         return ingresar()
     unidades = int(input(" Ingrese la Cantidad de unidades de el Producto : "))
     carrito.append({"nombre":nombre,"precio":precio,"unidades":unidades})
    except ValueError:
        print("\n Dato Ingresado No valido ")
#La funcion buscar recorre toda la lista y los diccionarios dentro de ella y si se encuentra se retorna un valor y seria un true,y si no retorna un vacio siendo un false y si es false dice que no esta y si es true muestra el producto con precio y unidades 
def buscar ():
    productoabuscar = input(" Ingrese el Producto que desa Buscar : ").lower()
    for producto in carrito:
        if productoabuscar == producto["nombre"] :
            print(" El Producto se encuentra dentro de el carrito :D ")
            return producto
    return None
#la funcion actualizar recorre el carrito y si encuentra que el producto es igual al input que se ingreso se pide el precio nuevo para actualizarlo y se cambia el precio viejo por el nuevo, si no se encuentra ninguno igual se le dice al usuario que no se encuentra en el carrito y que pruebe a ingresar el producto primero 
def actualizar ():
    try:
        productoabuscar = input(" Ingrese el Producto que desea Actualizar : ").lower().strip()
        for producto in carrito:
            if productoabuscar == producto["nombre"] :
                nvprecio = float(input("Ingrese el nuevo precio de el Producto : "))
                if nvprecio < 0 :
                    print (" Ingrese un Valor Positivo ")
                    return actualizar()
                producto["precio"] = nvprecio 
            else: 
                print(" El Producto no se encontro dentro de el carrito, intente ingresarlo primero ")
    except ValueError:
        print(" Dato Ingresado No valido ")
#La Funcion eliminar lo que hace es recorre la lista y si se encuentra un dato igual en los diccionarios de la lista elimina todo el diccionario que tiene ese dato eliminando asi tanto el nombre como precio y unidades 
def eliminar (): 
    Pelim = input(" Ingrese el Prodcuto que Desea Eliminar : ").lower().strip()
    for producto in carrito:
        if Pelim == producto["nombre"]:
            carrito.remove(producto)
            break
        else :
            print(" El Producto no se encuentra dentro de el Carrito ")
#La funcion imprimir se ejecuta cuando la persona selecciona la opcion salir y esta lo que hace es que recorre toda la lista y cada vez que entra a un diccionario suma la multiplicacion de unidades x precio y se van acumulando en una variable 
def imprimir () :
     total= sum(map(lambda p :p["precio"] * p["unidades"] , carrito))
     print (f" Total a Pagar : {total}")
#el menu principal ya este imprime el mensaje principal de el menu y las opcciones a ingresar, esta dentro de un ciclo para que siempre y cuando no ingrese la opccion de salir se vuelva y se muestre para seguir modificando o agregando cosas al programa.
while True :
    try:
     print("*"*40)
     menu = int(input(f"             MENU\n    Ingrese la Opcion que desea Realizar \n   Opcion 1 : Ingresar Productos al Carrito \n   Opcion 2 : Consultar Productos en el Carrito \n   Opcion 3 : Actualizar Precio de un Producto \n   Opcion 4 : Eliminar un Producto de el Carrito  \n   Opcion 5 : Salir del Programa    \n" ))
     if menu == 1 : 
        ingresar ()
     elif menu == 2: 
        productoBuscado = buscar ()
        if productoBuscado:
            print(productoBuscado)
        else:
            print("No se encontró")
     elif menu == 3 :
        actualizar()
     elif menu == 4 :
        eliminar()
     elif menu == 5 :
        imprimir()
        break
    except ValueError:
        print(" Ingrese Una Opcion Valida ")