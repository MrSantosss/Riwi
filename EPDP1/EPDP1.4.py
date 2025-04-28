#Pide dos números e indica cuál es mayor o si son iguales.
# Solicita una edad y determina si la persona es menor de edad (menor a 18).
# Escribe un programa que compare dos cadenas de texto e indique si son iguales o distintas.



num1 = int(input("Ingrese un numero : "))
num2 = int(input("Ungrese Otro numero : "))
if num1 == num2 :
    print("Los numeros ingresados son iguales :D ")
else :
    if num1 < num2 :
        print (f'{num2} es mayor que {num1}')
    else:
        print(f'{num1} es mayor que {num2}')



edad = int(input("Ingrese su edad :)  :"))
if edad < 18 : 
    print("Usted es menor asi q no va al taibol :c ")
else :
    print("Vamos pal taibol >:D ")
    
    
texto1 = input("Ingrese un texto : ")
texto2 = input("Ingrese otro texto : ")
if texto1 == texto2 :
    print("Ambos textos son iguales")
else: 
    print("Los textos no son identiocos")
    