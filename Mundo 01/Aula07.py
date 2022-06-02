#OPERADORES ARITMETICOS
# + , - , * , / , **(potencia) , //(divisao inteira)
# %
# RAIZ = 9**(1/2) -> quadrada 9**(1/3) -> cubica ...

#ORDEM DE PREDECENCIA
# 1 = ()
# 2 = **
# 3 = * , / , // , %
# 4 = + , -

#EXEMPLOS
# 5 + 3 * 2 = 11
# 3 * 5 + 4 ** 2 = 31
# 3 * (5 + 4) ** 2 = 243

nome = input('Qual eh o seu nome? ')
print('Prazer em te conhecer, {:=>20}!'.format(nome))

n1 = int(input('Insira um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma eh {}\nO produto eh {}, a divisao eh {:.3f}'.format(s, m, d), end=', ')
print('a divisao inteira eh {} e a potencia eh {}.'.format(di, e))
