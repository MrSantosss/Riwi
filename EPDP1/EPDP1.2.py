#Declara una variable de cada tipo básico: entero, flotante, cadena y booleano.
# Convierte una cadena con valor numérico a entero y realiza una suma con otro número.
# Convierte una entrada de texto a número flotante, multiplícala por 2 y muestra el resultado.
# Escribe una función que reciba un string y devuelva True si puede convertirse a número y False si no.

entero = int
flotante = float
cadena = str
booleano = bool

cadena1 = ("10")
cadena1 = int(cadena1)
cadena2 = cadena1+10 
print("Suma de su numero mas 10 : ",cadena2)

texto = input("Ingrese un numero por Multiplicar : ")
texto = float(texto)
textox2 = texto*2
print("Doble de Su numero : ",textox2)

texto_a_numero = input("Ingrese un texto o un numero : ")
funcion = False
try :
    valor = float(texto_a_numero) 
    funcion = True 
except ValueError: 
    funcion=False    
if funcion == True:
    print("Si se pudo")
else:
    print("pailas")



    
    



