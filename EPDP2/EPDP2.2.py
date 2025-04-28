nota = float(input("Ingrese Su Nota : "))

if nota == 0 :
    print ("Usted esta es pero llevado ")
elif nota < 0 :
    print ("Usted como va a tener una nota negativa wtf ")
elif  nota > 100 :
    print ("Su nota pasa los limites su eminencia ")
elif nota < 60 and nota > 0 :
    print ("Usted va perdiendo esto ")
elif nota >= 60 and nota <= 100 :
    print("Su nota esta mela ")