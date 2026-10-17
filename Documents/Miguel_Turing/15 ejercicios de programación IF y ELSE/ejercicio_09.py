precio = float(input("Ingrese el precio de la compra: "))

if precio >= 200000:
    descuento = precio * 0.20
elif precio >= 100000:
    descuento = precio * 0.10
else:
    descuento = 0.0

total = precio - descuento
print(f"Descuento aplicado: ${descuento}")
print(f"Total a pagar: ${total}")