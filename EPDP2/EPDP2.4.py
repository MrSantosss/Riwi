numero = int(input("Ingrese un número positivo para iniciar la cuenta regresiva: "))
if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
     while numero >= 0:
            print(numero)
            numero -= 1