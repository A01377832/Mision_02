#Ana Fernanda Martínez García, A01377832
# programa que calcula el costo total de una comida en un restaurante


subtotal= int(input ( "Ingrese el costo de la comida: "))

propina= subtotal*.16
IVA= subtotal* .13
Total= subtotal+propina+IVA

print( 'Propina: $%.02f' % (propina))
print( 'IVA: $%.02f' % (IVA))
print( 'Total de la comida: $%.02f' % (Total))