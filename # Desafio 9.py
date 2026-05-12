# Desafio 9
# faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada
n = int(input('Digite um numero: '))
tabuada = 0 + 1
resultado = n * tabuada
tempo = '{} X {} = {}' .format(n,tabuada,resultado)
print('A tabuada do numero {} é: '.format(n))
#print('{} X {} = {}' .format(n,tabuada,resultado))
for tempo in range(11):
    print(n, 'x', tabuada ,' =',tabuada * n)