# Desafio 15
# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = float(input('Quantos dias o carro foi alugado? '))
Km = float(input('Quantos Km esse carro percorreu? '))
totaldia = dia * 60
totalkm = Km * 0.15
resul = totaldia + totalkm
print('O total a pagar e de R${}'.format(resul))
