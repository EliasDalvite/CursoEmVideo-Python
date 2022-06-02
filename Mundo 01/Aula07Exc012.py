#ler preco do produto e mostrar ele com 5% de desconto
num = float(input('Qual o preco? '))
print('{} com 5% de desconto custa R${:.5}'.format(num,num-(num*0.05)))