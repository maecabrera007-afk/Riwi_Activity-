



while True:
    print("\nCAJERO AUTOMATICO\n")
    print("(1) Retiro")
    print("(2) Deposito")
    print("(3) Consulta de saldo")
    print("(4): Salir")

    print("\nDijite la opcion\n")

    Nombre = "Juan"
    Saldo = 25000000

    opcion = input()
    if opcion not in ["1","2","3","4"]:
        print("\nDebe ingresar una opcion valida")
        continue
    elif opcion == "4":
        break
    elif opcion == "1":
        deposito= float(input ("agrege el valor a retirar"))
        Saldo = Saldo - deposito
        print("Su nuevo saldo es: " + str(Saldo))

    elif opcion == "2":

        ingresarMonto= float(input ("agrege el valor a depositar"))
        Saldo = Saldo + ingresarMonto
        print("Su nuevo saldo es: " + str(Saldo))
    elif opcion == "3":
        print("Su saldo es de: "+ str(Saldo))