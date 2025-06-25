#Exercício Aula 16 - Tuplas

#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros_sorteados = (0, )
contador = 1
while(contador < 5):
    numero_sorteado = randint(1, 10)
    numeros_sorteados += numero_sorteado + ','
    contador += 1



print(numeros_sorteados)