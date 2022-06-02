#Faça um programa que leia algo pelo
#teclado e mostre na tela o seu tipo
#primitivo e todas as informações
#possíveis sobre ele.
x = input('Digite algo: ')
print('O tipo primitivo deste valor eh:',type(x))
print('Soh tem espacos?',x.isspace())
print('Eh numero?',x.isnumeric())
print('Eh alfabetico?',x.isalpha())
print('Eh alfanumerico?',x.isalnum())
print('Eh maiusiculo?',x.isupper())
print('Eh minusculo?',x.islower())
print('Esta capitalizada?',x.istitle())
