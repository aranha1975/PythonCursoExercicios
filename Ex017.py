from math import hypot
cad=float(input('Insira a medida do cateto adjacente do triângulo retângulo: '))
cop=float(input('Insira a medida do cateto oposto de triângulo retângulo: '))
print('A medida da hipotenusa desse mesmo triângulo retângulo é {:.2f}.'.format(hypot(cad,cop)))

