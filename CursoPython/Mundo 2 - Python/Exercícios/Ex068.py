#Aula 15 - Interrompendo repetições while

#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
#que ele conquistou no final do jogo.

from random import randint

derrota = 0
vitoria = 0
partida = 0

while(derrota == 0):
    partida += 1
    computador = randint(0, 10)
    print(f"{f'Partida nº{partida}':=^20}")
    par_impar = str(input(f"Par ou Ímpar: [P/I] ")).lower().strip()[0]
    if(par_impar == "p"):
        numero = int(input(f"Você é par, digite um número: "))

    else:
        numero = int(input(f"Você é ímpar, digite um número: "))

    print(f"-" * 10)
    verificacao = computador + numero
    print(f"Você jogou {numero} e o computador jogou {computador}, total é {verificacao}")
    print(f"-" * 10)
    if((verificacao % 2 == 0) and (par_impar == "p")):
        print(f"Você venceu!")
        print(f"{verificacao} é Par!")
        vitoria += 1
    elif((verificacao % 2 != 0) and (par_impar == "i")):
        print(f"Você venceu!")
        print(f"{verificacao} é Ímpar!")
        vitoria += 1
    