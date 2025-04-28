#Solicita el nombre y edad del usuario, luego imprime un saludo personalizado que incluya ambos datos. 
# Pide al usuario que ingrese su comida favorita y su color favorito, luego imprime una frase con ambos.
# Solicita un número y muestra su doble y su triple

nombre = input("Ingrese Su Nombre : ")
edad = int(input("Ingrese Su Edad : "))
print(" ¡Hola ", nombre, "! Tu Edad Actual es : ", edad )

comida = input("Ingrese Su Comida Favorita : ")
color = input("Ingrese Su Color Favorito : ")
print("Tal vez te Fascine ir a comer ",comida , "en algun lugar completamente ",color)

numero = int(input("Ingrese su Numero preferido : "))
print ("Numero Original : ",numero, "Doble : ",numero*2 , "Triple : ",numero*3 )

