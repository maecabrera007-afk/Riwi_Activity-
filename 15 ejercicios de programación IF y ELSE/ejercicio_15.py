cliente = input("Nombre del cliente: ")
producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad

if subtotal >= 500000:
    descuento = subtotal * 0.15
elif subtotal >= 200000:
    descuento = subtotal * 0.10
else:
    descuento = 0.0

total = subtotal - descuento

print("\n--- FACTURA DE VENTA ---")
print(f"Cliente: {cliente}")
print(f"Producto: {producto} (Cantidad: {cantidad})")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Descuento aplicado: ${descuento:,.2f}")
print(f"Total a pagar: ${total:,.2f}")