print("   Adivina el Numero    ")
intentos = 3 
xadivinar = 7

while intentos > 0 :
        intento = int(input("Ingrese un Numero en 0 y 10 : "))
        if intento < 0 or intento > 10 :
         print (" Numero Fuera de el Rango D:<")
        if intento>xadivinar :
            print ("El Numero es Menor")
        elif intento<xadivinar : 
                print("El Numero es Mayor")
        elif intento==xadivinar :
             print(" ADIVINANSTE EL NUMEROO ")
        intentos -=1
        if intentos == 0 :
            print (f"Agotaste los Intentos el numero era {xadivinar}")


