num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")

if suma > 10:
    print("La suma es mayor que 10.")
else:
    print("La suma no es mayor que 10.")