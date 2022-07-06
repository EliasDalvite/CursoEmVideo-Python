# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1 = float(input('Numero 1:'))
n2 = float(input('Numero 2:'))
n3 = float(input('Numero 3:'))
n4 = float(input('Numero 4:'))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('Nova ordem:')
print(lista)