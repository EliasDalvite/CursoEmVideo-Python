from math import sqrt
import random
import emoji
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}!'.format(num, raiz))
num = random.randint(1, 10)
print(emoji.emojize('Uepa :sunglasses:!', use_aliases=True))
