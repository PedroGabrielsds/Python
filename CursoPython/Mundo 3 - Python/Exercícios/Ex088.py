#Aula 18 - Listas Parte 2

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados
#e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

palpites = []
auxiliar = []
contador = 1

print("-" * 30)
print(f"{f"MEGA SENA":^30}")
print("-" * 30)

jogos = int(input(f"Quantos jogos deseja fazer? "))

while contador <= jogos:
    contador += 1
    for c in range(1, 7):
        print(contador)
        num = randint(1,60)
        if(num not in auxiliar):
            auxiliar.append(num)
        if(len(auxiliar) == 6):
            palpites.append(auxiliar[:])
    auxiliar.clear()

print("-=" * 3, end=" ")
print(f"{f" SORTEANDO {jogos} JOGOS ": ^5}", end=" ")
print("-=" * 3)

contador = 1
for jogo in palpites:
    jogo.sort()
    print(f"Jogo {contador}: {jogo}")
    sleep(1)
    contador += 1

print(f"-=" * 4, end=" ")
print(f" < BOA SORTE! > ", end=" ")
print(f"-=" * 4)

#consertar lógica da geração de jogos