librerias = []

def ingresarlibros():
    while True:
        try:
            titulo = input("Ingrese el Título del Libro: ").lower().strip()
            genero = input("Ingrese el Género del Libro: ").lower().strip()
            unidades = int(input("Ingrese la Cantidad de Unidades que Ingresarás: "))
            if unidades < 0:
                print("Ingrese una cantidad de unidades válida.")
                continue
            librerias.append({"titulo": titulo, "genero": genero, "unidades": unidades, "copiastotal": unidades})
            break
        except ValueError:
            print("Ingrese un dato válido.")

def buscarlibro():
    buscar_titulo = input("Ingrese el Título del Libro que desea Buscar: ").lower().strip()
    for libro in librerias:
        if libro["titulo"] == buscar_titulo:
            print(f"\nEl libro '{libro['titulo']}' está en la librería.\n")
            return libro
    print("\nEl libro no se encuentra en la biblioteca.\n")
    return None

def prestarlibro():
    libroprestar = input("Ingrese el nombre del libro que desea prestar: ").lower().strip()
    for libro in librerias:
        if libro["titulo"] == libroprestar:
            if libro["unidades"] > 0:
                libro["unidades"] -= 1
                print(f"Usted prestó una unidad de '{libro['titulo']}'.")
            else:
                print("\nEl libro ingresado no tiene unidades disponibles.\n")
            return
    print("\nEste libro no existe en la biblioteca.\n")

def devolverlibro():
    librodevolver = input("Ingrese el nombre del libro que quieres devolver: ").lower().strip()
    for libro in librerias:
        if libro["titulo"] == librodevolver:
            if libro["unidades"] < libro["copiastotal"]:
                libro["unidades"] += 1
                print(f"Usted regresó una unidad del libro '{libro['titulo']}'.")
            else:
                print(f"\nEl libro '{libro['titulo']}' tiene todas sus unidades en la biblioteca. Esta unidad no nos pertenece.\n")
            return
    print("\nEl libro no se encuentra en esta biblioteca.\n")

def eliminarlibro():
    libroeliminar = input("Ingrese el libro que quieres eliminar de la biblioteca: ").lower().strip()
    for libro in librerias:
        if libro["titulo"] == libroeliminar:
            if libro["unidades"] == libro["copiastotal"]:
                librerias.remove(libro)
                print("\nEl libro fue eliminado de la biblioteca correctamente.\n")
            else:
                print(f"\nAún no están todas las copias del libro '{libro['titulo']}' en la biblioteca (Aún hay copias alquiladas).\n")
            return
    print("\nEl libro ingresado no se encuentra en la biblioteca.\n")

def listagenero():
    listagen = input("Ingrese un género para ver los libros disponibles: ").lower().strip()
    encontrados = False
    for libro in librerias:
        if libro["genero"] == listagen:
            print(libro)
            encontrados = True
    if not encontrados:
        print(f"No se encontraron libros del género '{listagen}'.")

def inventario():
    print("*" * 20)
    print("INVENTARIO")
    for libro in librerias:
        print(libro)
while True:
    try:
        print("\n--- BIBLIOTECA ---")
        print("1: Ingresar Libros a la Librería")
        print("2: Buscar Libros en el Inventario")
        print("3: Buscar Libros Disponibles por Género")
        print("4: Prestar Libros de la Biblioteca")
        print("5: Regresar Libros a la Biblioteca")
        print("6: Eliminar un Título de la Biblioteca")
        print("7: Mostrar todo el Inventario de la Biblioteca")
        print("8: Terminar el programa")
        opcion = int(input("Seleccione una opción: "))
            
        if opcion == 1:
            ingresarlibros()
        elif opcion == 2:
            buscarlibro()
        elif opcion == 3:
            listagenero()
        elif opcion == 4:
            prestarlibro()
        elif opcion == 5:
            devolverlibro()
        elif opcion == 6:
            eliminarlibro()
        elif opcion == 7:
            inventario()
        elif opcion == 8:
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
                print("Ingrese una opción válida (1-8).")
    except ValueError:
            print("Ingrese un número válido para la opción.")