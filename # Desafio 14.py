# Desafio 14
# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Informe uma temperatura em °C: '))
f = celsius * 1.8 + 32
print('A temperatura de {}°C corresponde a {}°F'.format(celsius,f))
