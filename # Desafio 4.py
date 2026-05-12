# Desafio 4
#  Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input("digite algo: ")
print("O tipo primitivo desse valor é: ", type(a))
print('So tem espaços? ', a.isspace())
print('E um numero ? ', a.isnumeric())
print('E alfabetico ? ', a.isalpha())
print('E alfanumerico? ', a.isalnum())
print('Esta em maiusculas? ', a.isupper())
print('Esta em minusculas? ', a.islower())
print('Esta capitalizada? ', a.istitle())