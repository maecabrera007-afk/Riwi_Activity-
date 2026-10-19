Nombre_cliente = input("cual es su nombre ")
Nombre_producto = input("cual es el nombre del producto ")
Tl= float (input("Digite el valor del producto: "))
cantidad= int (input("Digite la cantidad de productos a llevar "))


Total = Tl * cantidad
print("El producto seria: " + str(Total))

if Total < 200000:
    print("No aplica descuento ")
elif Total >= 200000 and Total < 500000:
    #print("El descuenyo es del 10")
    Descuento = (Total*-0.10)+Total
    #print(Descuento)
elif Total >= 500000:
    #print("El descuento es del 20")
    Descuento = (Total*-0.20)+Total
   # print(Descuento)


print ("--------------------------------")
print ("          Factura")
print ("--------------------------------")
print("Cliente: " + Nombre_cliente)
print("Cliente: " + Nombre_producto)
print("Cantidad a llevar: "+ str(cantidad))
print("Total a pagar: " +str(Descuento))