# Autor: Ana Fernanda Martínez, A01377832
# Descripcion: Calcular timepo o distancia de un auto en movimiento


v = float(input ("Ingrese velocidad en enteros: "))
t1= 6
d1= v*t1

t2= 3.5
d2= v*t2

d3= 485
t3= d3/v


print( '%.02f, km' % (d1))
print( '%.02f, km ' % (d2))
print( '%.02f, hrs' % (t3))

