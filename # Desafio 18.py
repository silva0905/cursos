 # Desafio 18
 # Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#angulo = float(input('Digite um angulo que deseja: '))
import math

angulo = float(input("Digite o ângulo em graus: "))
radianos = math.radians(angulo)
print(f"Seno: {math.sin(radianos):.2f}")
print(f"Cosseno: {math.cos(radianos):.2f}")
print(f"Tangente: {math.tan(radianos):.2f}")