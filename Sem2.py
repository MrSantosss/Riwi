#Primero se Pide la Lista de notas separado por comas 
notas = 0
calificaciones = input("Ingrese las Notas a Promeditar Separadas por coma (,): ").split(",")
#Se ingresan en una lsita transformando los valores en float
lista_calificacion = []
for calificacion in calificaciones :
    lista_calificacion.append(float(calificacion))
#Se recorre la lista y se organizan las notas para mostrarlas junto a la cantidad de notas que ingreso 
#y el promedio de estas mismas 
for calificacion in lista_calificacion :
 notas += calificacion 
print(f"Calificaciones Inngresadas : {lista_calificacion}") 
print (f"Cantidad De Notas Ingresadas ({len(lista_calificacion)})")
print ((f"Promedio de las notas ingresadas : {notas / len(lista_calificacion)}"))


#Se pide una nota para validar cuantas notas en la lista son mayor que esta 
e= 0 
h= 0
# se inicializan variables para tenerlos como contador si se cumple el mayor o el menor q 
mayorq = float(input("Ingrese una Nota para ver cuantas notas son mayores : "))
for calificacion in lista_calificacion:
    if  calificacion > mayorq : 
        e+=1 
    else: 
        h+=1
#se printea la cantidad de veces que se modifico las variables anteriormente inicializadas
print(f"Cantidad De Notas Mayores a la Ingresada ({e}) ")
print(f"Notas Menores a la nota ingresada ({h}) ")

#igualmente se inicializa otra variable para modificarla
k=0
#cada que una nota sea igual ala que se ingreso se modifica la variable y 
#luego se immprime 
encontrar = float(input("Ingrese la Nota que desea Buscar en la Lista  : "))
for calificacion in lista_calificacion :
     if calificacion == encontrar :
         k += 1
print(f"Su nota se encuentra {k} veces en la Lista ")
# se ingresa la nota de el promedio y se valida si gana o pierde 
nota = float(input("Ingrese Su Nota ( En el Rango entre 0 y 100 ) : "))
if nota < 0  or nota > 100 :
    print (" Ingrese un Numero dentro de el rango >:c")
else:
    if nota == 0 :
     print ("Usted esta es pero llevado ")
    elif nota < 60 and nota > 0 :
     print ("Usted va perdiendo  ")
    elif nota >= 60 and nota <= 100 :
     print("Usted va Ganando")