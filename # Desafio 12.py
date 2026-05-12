# Desafio 12
# Faça um algoritmo que  leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Qual e o preço do produto? '))
desconto = 5 / 100
total = desconto * preco
resultado = preco - total
print('O seu preço  antigo sem desconto foi de {} reais, para {} reais'.format(preco,resultado))
