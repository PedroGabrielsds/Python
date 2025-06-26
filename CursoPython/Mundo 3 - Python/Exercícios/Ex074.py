#Exercício Aula 16 - Tuplas

#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
maior = 0
menor = 0
contador = 0

numeros_aleatorios = (randint(1,10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f"Números gerados foram:", numeros_aleatorios)
for numero in numeros_aleatorios:
    contador += 1
    if(contador == 1):
        menor = numero
        maior = numero
    else:
        if(numero > maior):
            maior = numero
        elif(numero < menor):
            menor = numero

print(f"O maior número gerado é: {maior}")
print(f"O menor número gerado é: {menor}")