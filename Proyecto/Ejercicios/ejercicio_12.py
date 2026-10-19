print ("Digite tres lados de un triangulo que sean enteros")

L1 = float (input ("lado 1: "))
L2 = float (input ("lado 2: "))
L3 = float (input ("lado 3: "))

if L1 == L2 and L1 == L3 :
    print("El triangulo es Equilatero")
elif L1 != L2 and L1 != L3 and L2 != L3 :
    print("El triangulo es Escaleno")
elif (L1 == L2 and L1 != L3) or( L3 == L2 and L3 != L1) or( L1 == L3 and L1 != L2): 
    print ("El triangulo es Isoceles")