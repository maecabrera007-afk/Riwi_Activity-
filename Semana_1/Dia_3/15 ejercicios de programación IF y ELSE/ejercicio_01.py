nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print(f"Nombre: {nombre}")
if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")