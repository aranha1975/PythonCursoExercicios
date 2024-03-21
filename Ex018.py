import math
from math import sin, cos, tan, radians
ang=float(input('Insira um ângulo: '))

rad=radians(ang)
#rad=0.0174533*ang - essa é outra alternativa pra conversão em radianos, pois 1 graus equivale a 0,0174533

print("O seno do ângulo {} vale {:.2f}\nO coseno vale {:.2f}\nA tangente vale {:.2f}".format(ang, sin(rad), cos(rad), tan(rad)))


