# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import math
import random
a1 = input('1o aluno: ')
a2 = input('2o aluno: ')
a3 = input('3o aluno: ')
a4 = input('4o aluno: ')
lista = [a1,a2,a3,a4]
print('Aluno sorteado: {}'.format(random.choice(lista)))