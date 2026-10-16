saldo = 500000

print("--- CAJERO AUTOMÁTICO ---")
print("1. Consultar saldo")
print("2. Retirar dinero")
print("3. Depositar dinero")
print("4. Salir")

opcion = input("Seleccione una opción (1-4): ")

if opcion == '1':
    print(f"Su saldo actual es: ${saldo:,.2f}")
elif opcion == '2':
    retiro = float(input("Ingrese la cantidad a retirar: "))
    if retiro > saldo:
        print("Error: Fondos insuficientes.")
    elif retiro <= 0:
        print("Error: Cantidad inválida.")
    else:
        saldo -= retiro
        print(f"Retiro exitoso. Nuevo saldo: ${saldo:,.2f}")
elif opcion == '3':
    deposito = float(input("Ingrese la cantidad a depositar: "))
    if deposito <= 0:
        print("Error: Cantidad inválida.")
    else:
        saldo += deposito
        print(f"Depósito exitoso. Nuevo saldo: ${saldo:,.2f}")
elif opcion == '4':
    print("Gracias por usar el cajero automático. ¡Hasta luego!")
else:
    print("Opción no válida.")