# Desafio 17
#  Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
cat = float(input("Comprimeito do cateto oposto : "))
catad = float(input('Comprimento do cateto adjacente: '))
soma = (cat ** 2) + (catad ** 2)
resultado = soma**0.5
print ('A hipotenusa vai medir:{:.2f}'.format(resultado))
#raiz = numero ** 0.5