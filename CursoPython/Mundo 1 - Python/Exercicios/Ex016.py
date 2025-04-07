#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
numero = float(input("Digite um número real qualquer: "))

print(F"A parte inteira de {numero} é {trunc(numero)}!")

"""Outra forma de fazer o exercicio anterior"""

"""print(f"A parte inteira é {int(numero)}")"""