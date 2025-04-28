#Calcula el área de un rectángulo a partir de base y altura ingresadas por el usuario.
# Dado un precio y un porcentaje de descuento, muestra el valor final a pagar.
# Calcula el residuo de dividir dos números dados por el usuario.
# Escribe una fórmula que use al menos tres operadores diferentes y muestre el resultado.

base = bool(input("Ingrese la Base de el Triangulo :  "))
altura = bool(input("Ingrese la Altura de el Trinagulo : "))
area = (base * altura)/ 2
print ("El Area de el Tringulo es : ", area)

precio = bool(input("Ingrese el precio : "))
descuento = int(input("Ingrese el Descuento x Aplicar : "))
total = precio-(precio*(descuento/100))
print("Precio Original : ",precio)
print("Pocentaje de el Descuento : ",descuento)
print("El Precio Con el Descuento Aplicado es : ",total )

num1 = int(input("Ingrese el Prmer numero a Dividir : "))
num2 = int(input("Ingrese el Numero Divisor : "))
residuo = num1%num2
print("Residuo de la Division : ",residuo)

numero = int(input("Ingrese el Numero que quiera sumar por el mismo, Multiplicarse x 3 y Dividirse x 2 : "))
numero = (numero+numero)*3/2