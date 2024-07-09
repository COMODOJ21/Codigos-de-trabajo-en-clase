# COSTA AZULL
precio_camisa = 35.000
precio_pantalon = 75.000 
descuento_porcentaje = 14 / 100 

# SACAR EL PORCENTAJE
subtotal = precio_camisa + precio_pantalon
descuento = subtotal * descuento_porcentaje
total = subtotal - descuento

#CELULAR EN TIGO
precio_celular = 900.000
#FINAL DE TOTAL
gasto_total = total + precio_celular

print(f"Subtotal en Costa Azul: ${subtotal:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar en Costa Azul después del descuento: ${total:.2f}")
print(f"Gasto total en el día de compras: ${gasto_total:.2f}")