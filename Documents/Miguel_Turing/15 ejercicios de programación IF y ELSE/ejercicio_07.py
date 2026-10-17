edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Error: La edad no puede ser negativa.")
elif edad >= 18:
    print("Puede ingresar al evento para mayores de 18 años.")
else:
    print("No puede ingresar, es menor de edad.")