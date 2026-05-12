# Desafio 13
# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
salario = float(input('Qual e o seu salario? '))
aumento = 15 / 100
total = salario * aumento
resultado = salario + total
print('O seu salario de {} Reais, Recebeu um aumento de 15%'.format(salario))
print('O Seu novo salario e de {} Reais'.format(resultado))