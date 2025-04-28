#Pide al usuario su edad y si tiene licencia de conducción. Solo si ambas condiciones se cumplen, imprime que puede conducir.
# Solicita si una persona tiene experiencia laboral y título universitario. Usa operadores lógicos para decidir si puede aplicar a una oferta de trabajo.
# +Dado un número, determina si está en el rango de 10 a 50 (inclusive).

edad = int(input("Ingrese su edad : "))
licencia = input("Tiene usted licencia de Conduccion ?  (Si o No)  : ").upper()
if edad > 17 and licencia == "SI" :
    print("Ustde es mayor de Edad y Porta Licencia :D ")
else:
    if edad < 17 or edad == 17 and licencia == "SI":
        print ("Usted es menor de edad pero Ya tiene Licencia :D ")
    else : 
        if edad >17 and licencia == "NO":
            print("Usted es Mayor de edad pero Aun no Tiene Licencia :c ")
        else:
            if edad <17 or edad == 17 and licencia=="NO":
                print("Usted es Menor de edad y Aun no tiene licencia ")
                
                
Experiencia = input("Posee usted Eperiencia laboral ? (Si o No) : ").upper()
Titulo = input("Posee usted un Titulo Universitario ? (Si o No ) : ").upper()

if Experiencia == "SI" and Titulo == "SI" :
    print("Usted Puede Aplicar a un Empleo que Pida Experiencia y Titulo Universitario  ")
else:
    if Experiencia == "NO"  and Titulo == "SI":
        print ("Usted puede Aplicar a un Empleo que no soliciten Experiencia ")
    else : 
        if Experiencia == "SI" and Titulo == "NO":
            print("Usted puede Aplicar a un Empleo que no soliciten Titulos Universitarios ")
        else:
            if Experiencia == "NO" and Titulo =="NO":
                print("Usted puede Aplicar a Empleos que No pidan Experiencia Ni Titulos Universitarios ")



numero = int(input("Ingrese un numero : "))
if numero >=10 and numero <= 50 :
    print("Su numero esta en el rango de 10 a 50 ")
else :
    print("Su numero es uno fuera del rango entre 10 y 50")
    