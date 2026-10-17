a = float(input("Ingrese el primer lado: "))
b = float(input("Ingrese el segundo lado: "))
c = float(input("Ingrese el tercer lado: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Es un triángulo válido.")
    if a == b == c:
        print("Clasificación: Equilátero.")
    elif a == b or b == c or a == c:
        print("Clasificación: Isósceles.")
    else:
        print("Clasificación: Escaleno.")
else:
    print("Error: Los lados ingresados no forman un triángulo válido.")