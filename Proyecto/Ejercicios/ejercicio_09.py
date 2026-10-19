compra = input("Digite el valor de su compra: ")

compra = float(compra)

if compra < 100000:
    print("Su compra no tiene descuento")
elif compra >=100000.0 and compra < 200000.0:
    print("Su compra tiene el 10 de descuento")
    Descuento = compra*0.10
    Total = compra - Descuento

    print("Su compra queda en: " +str(Total))
    
elif compra > 200000.0:
    print("Su compra tiene el 20 de descuento")
    Descuento =compra*0.20
    Total = compra - Descuento
    print("Su compra queda en: " +str(Total))
