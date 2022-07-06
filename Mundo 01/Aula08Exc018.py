#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o ângulo: '))
seno =  math.sin( math.radians(angulo))
cosseno =  math.cos( math.radians(angulo))
tangente = math.tan( math.radians(angulo))
print('Seno de {}: {:.8}'.format(angulo, seno))
print('Cosseno de {}: {:.8}'.format(angulo, cosseno))
print('Tangente de {}: {:.8}'.format(angulo, tangente))

