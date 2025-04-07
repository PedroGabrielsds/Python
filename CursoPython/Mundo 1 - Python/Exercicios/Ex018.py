#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo_graus = float(input("Digite um ângulo em graus: "))

angulo_radiano = float(math.radians(angulo_graus))
seno = float(math.sin(angulo_radiano))
cosseno = float(math.cos(angulo_radiano))
tangente = float(math.tan(angulo_radiano))

print(f"O seno de {angulo_graus} é: {seno:.2f}")
print(f"O cosseno de {angulo_graus} é: {cosseno:.2f}")
print(f"A tangente de {angulo_graus} é: {tangente:.2f}")



