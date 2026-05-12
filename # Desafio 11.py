# Desafio 11
# Faça um programa que leia a largura e a altura de uma parede  em metros , calcule a sua area e a quantidade de tinta necessaria para pinta-la
# Sabendo que cada litro  de tinta pinta uma area de 2mquadrados
alt = float(input('Qual e a altura da sua parede? '))
larg = float(input('Qual e a largura da sua parede? '))
area = alt * larg
tinta = area / 2
print('A area da sua parede e igual a {:.1f} metros quadrados'.format(area))
print('Para pintar a area de {} metros é necessario {} litros de tinta '.format(area,tinta))