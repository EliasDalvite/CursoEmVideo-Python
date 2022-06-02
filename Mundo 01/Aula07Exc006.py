#leia um numero, mostre o dobro, o triplo e a raiz quadrada
n = int(input('Insira o numero: '))
print('{} X 2 = {}\n{} X 3 = {}\nRaiz quadrada de {} = {:.8}'.format(n,n*2,n,n*3,n,n**(1/2)))