#Aula 15 - Interrompendo repetições while

#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
#que ele conquistou no final do jogo.

from random import randint
from time import sleep

resposta = "s"

while(resposta != "n"):
    vitoria = 0
    partida = 0
    cor = 30
    cor_pontos = 30
    derrota = False
    while(derrota == False):
        cor += 1
        partida += 1
        computador = randint(0, 10)
        print(f"{f'\033[1;{cor};40mPartida nº{partida}\033[m':=^43}")
        par_impar = str(input(f"\033[1;33mPar ou Ímpar\033[m: [P/I] ")).lower().strip()[0]
        if(par_impar == "p"):
            numero = int(input(f"Você é par, \033[1;33mdigite um número\033[m: "))
        else:
            numero = int(input(f"Você é ímpar, \033[1;33mdigite um número\033[m: "))
        print(f"-" * 30)
        verificacao = computador + numero
        print(f"Você jogou {numero} e o computador jogou {computador}.", end=" ")
        if(verificacao % 2 == 0):
            print(f"Total é {verificacao} que é Par!")
            print(f"-" * 30)
            if(par_impar == "p"):
                print(f"\033[1;32;40mVocê Venceu\033[m!")
                print(f"\033[1;34mVamos jogar novamente\033[m", end="")
                cor_pontos = 30
                vitoria += 1
                for contador in range(1, 3 + 1):
                    if(contador != 3):
                        cor_pontos += 1
                        print(f"\033[1;{cor_pontos}m.\033[m", end="")
                        sleep(1)
                    else:
                        cor_pontos += 1
                        print(f"\033[1;{cor_pontos}m.\033[m")
                        sleep(1)
            else:
                print(f"\033[1;31;40mVocê Perdeu\033[m!")
                derrota = True
                break
        else:
            print(f"Total é {verificacao} que é Ímpar!")
            print(f"-" * 30)
            if(par_impar == "i"):
                print(f"\033[1;32;40mVocê Venceu\033[m!")
                print(f"\033[1;34mVamos jogar novamente\033[m", end="")
                vitoria += 1
                for contador in range(1, 3 + 1):
                    if(contador != 3):
                        cor_pontos += 1
                        print(f"\033[1;{cor_pontos}m.\033[m", end="")
                        sleep(1)
                    else:
                        cor_pontos += 1
                        print(f"\033[1;{cor_pontos}m.\033[m")
                        sleep(1)
            else:
                print(f"\033[1;31;40mVocê Perdeu\033[m!")
                derrota = True
                break
    if(derrota == True):
        resposta = str(input(f"Deseja jogar novamente? [S/N] ")).lower().strip()[0]
        if(resposta == "n"):
            break

if(vitoria == 0):
    print(f"\033[1;31mVocê não venceu nenhuma partida\033[m!")
else:
    if(vitoria == 1):
        print(f"\033[1;32mVocê ganhou {vitoria} partida\033[m!")
    elif(vitoria > 1):
        print(f"\033[1;32mVocê ganhou {vitoria} partidas seguidas\033[m!")
print(f"\033[1;31;mFinalizando Par ou Ímpar\033[m...")