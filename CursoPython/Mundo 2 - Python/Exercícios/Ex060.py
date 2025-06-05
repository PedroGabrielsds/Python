#Aula 14 - Estrutura de repetição While

#Faça um programa que leia um número qualquer e mostre o seu fatorial
#Ex: 5! = 5x4x3x2x1 = 120

from math import factorial

numero = int(input(f"Fatorial de "))

print(f"{numero}! =", end=" ")
for contador in range(numero, 0, - 1):
    if (contador == 1):
        print(f"{contador} = {factorial(numero)}")
    else:
        print(f"{contador} x", end=" ")