#pede cateto oposto, adjacente, e mostra a hipotenusa
from math import sqrt, pow
catOposto = float(input('Comprimento do cateto oposto: '))
catAdjacente = float(input('Comprimento do cateto adjacente: '))
print('Hipotenusa vai medir {:.2f}!'.format(sqrt(pow(catOposto, 2)+pow(catAdjacente, 2))))
# tbm tem "math.hypot(catOposto, catAdjacente)" q retorna o result da hipotenusa :)
