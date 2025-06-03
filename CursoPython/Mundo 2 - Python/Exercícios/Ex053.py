#Ex053 - Aula 13

#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: Apos a sopa
#A sacada da casa
#A torre da derrota
#O lobo ama o bolo
#Anotaram a data da maratona

from time import sleep

frase = "o lobo ama o bolo"
print(frase)
frase_dividida = frase.split()
frase_sem_espaco = "".join(frase_dividida)
tamanho_frase = int(len(frase_sem_espaco))

frase_reversa = ""

#for letra in range(0, tamanho_frase + 1, 1):
print(f"\033[1:32:40m{frase_sem_espaco[0::]}\033[m", end="")

 #   sleep(0.3)

print(f" ")

for letra in range(tamanho_frase, -1, - 1):
    print(f"\033[1;31;40m{frase_sem_espaco[letra - 1: letra]}\033[m", end="")
    frase_reversa += frase_sem_espaco[letra - 1: letra]
    sleep(0.3)

print(" ")
print(frase_reversa)