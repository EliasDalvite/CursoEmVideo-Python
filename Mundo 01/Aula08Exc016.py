#ler um valor e mostrar a porcao inteira
from math import trunc
num = float(input('Manda o numero: '))
print('O valor digitado foi {} e sua porção inteiro é {}!'.format(num, trunc(num)))
#da pra meter um ".format(num, int(num))", q dai n importa nada, deixa mais leve :)
