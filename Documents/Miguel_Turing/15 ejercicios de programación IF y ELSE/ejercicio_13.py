print("--- MENÚ DE CALCULADORA ---")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Seleccione una opción (1-4): ")

if opcion in ['1', '2', '3', '4']:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print(f"Resultado: {num1 + num2}")
    elif opcion == '2':
        print(f"Resultado: {num1 - num2}")
    elif opcion == '3':
        print(f"Resultado: {num1 * num2}")
    elif opcion == '4':
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Error: División entre cero no permitida.")
else:
    print("Opción no válida.")