#Escreva um programa que pergunte a quantidade de Km percorridos
#por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
quantDias = int(input('Por quantos dias tal carro foi alugado?'))
quantKm = float(input('Quantos quilômetros foram rodados?'))
precoTotal = (60*quantDias) + (0.15*quantKm)
print('O preço a pagar será de R${:.2f}!'.format(precoTotal))
