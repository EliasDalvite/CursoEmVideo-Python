from math import sqrt
import random
import emoji
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.8}!'.format(num, raiz))
num = random.randint(1, 10)
print('Numero aleatorio gerado:', num)
print(emoji.emojize('Uepa :sunglasses:!', use_aliases=True))
