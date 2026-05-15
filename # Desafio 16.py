# Desafio 16
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
real = float(input('Digite um valor: '))
print('O valor digitado foi  {} e a sua porção inteira é {} '.format(real,math.trunc(real)))
