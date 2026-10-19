N1 = float(input(" Digita un numero "))
N2 = float(input(" Digita un numero "))


if N1 == 0 or N2 ==0:
    print(" Ningun numero puede ser cero")

 # Crea un bucle infinito que se repetirá todo el tiempo
print("Elija la operacion que le gustaria realizar")
print("opcion 1 = *")
print("opcion 2 = -")
print("opcion 3= /") 
print("opcion 4 = +") 
    

eleccion = input ("Elija una opcion 1,2,3,4: ")
   
if eleccion == "1" :
    print("La multiplicacion es: "+N1*N2)
if eleccion == "2":
    print("la resta es: "+ N1-N2)
if eleccion == "3":
    print ("La division es: "+N1 /N2)
if eleccion == "4":
    print("Suma es: "+ N1 + N2)

