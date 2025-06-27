#Exercício Aula 16 - Tuplas

#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
maior = 0
menor = 0
contador = 0

numeros_aleatorios = (randint(1,10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f"Os números gerados foram: ", end="")
for posicao, numero_aleatorio in enumerate(numeros_aleatorios):
    if(posicao != 4):
        print(f"{numero_aleatorio}", end=", ")
    else:
        print(f"{numero_aleatorio}", end=" ")

print(f"\nO maior número sorteado foi {max(numeros_aleatorios)}")
print(f"O menor número gerado foi {min(numeros_aleatorios)}")