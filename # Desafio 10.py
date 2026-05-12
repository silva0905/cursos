# Desafio 10
# Crie um programa que leie quanto de dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# Considere o dolar = US$1,00 = R$ 3, 27
reais = float(input('Quantos reais vc tem na carteira? '))
cotacao  = 3.27
dolar = reais / cotacao 
print ('Com {} reais vc pode comprar {:.2f} dolares'.format(reais,dolar))


