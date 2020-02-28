# Ana Fernanda Martínez García, A01377832
# programa que calcula el porcentaje de hombres y mujeres inscritos en una clase.

# Escribe tu programa después de esta línea.

mujeres= int(input("Ingrese el número de mujeres inscritas: "))
hombres= int(input("Ingrese el número de hombres inscritos: "))

total= mujeres+hombres
porcentajem= mujeres*100/total
porcentajeh= hombres*100/total

print ("Total Inscritos:", total)

print("Porcentaje de mujeres: %.01f porciento" % (porcentajem))
print("Porcentaje de hombres: %.01f porciento" % (porcentajeh))