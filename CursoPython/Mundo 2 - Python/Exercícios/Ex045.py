#Ex045

#Exercicio Aula 12 - Condições Aninhadas

#Crie um programa que faça o computador jogar jokenpô(Pedra, Papel e tesoura) com você.

import random

print("\033[1;31;40m=--\033[m" * 5,"JOKENPÔ", "\033[1;31;40m--=\033[m" * 5)

jogadas = [1, 2, 3]
maquina = random.choice(jogadas)
print(maquina)
if (maquina == 1):
    computador = "Pedra"
elif (maquina == 2):
    computador = "Papel"
elif (maquina == 3):
    computador = "Tesoura"
else:
    print("\033[1;31;40mError!!\033[m")

jogador = str(input("\033[1;33;40mQual seu nickname? \033[m"))

escolha = int(input("""\033[1;37;40m[1] - Pedra\033[m 
\033[1;38;40m[2] - Papel\033[m
\033[1;31;40m[3] - Tesoura\033[m
\033[1;33;40mEscolha sua jogada:\033[m """))

if(escolha == 1):
    escolha_jogador = "Pedra"
elif(escolha == 2):
    escolha_jogador = "Papel"
elif(escolha == 3):
    escolha_jogador = "Tesoura"
else:
    print("\033[1;31;40mOpção inválida tente novamente...\033[m")

if(maquina == escolha):
    print(f"Máquina: {computador}")
    print(f"{jogador}: {escolha_jogador}")
    print(f"Empate!! Tente novamente...")
else:
    print("\033[1;37;40mJo\033[m")
    print("\033[1;38;40mKen\033[m")
    print("\033[1;31;40mPô!\033[m")

    if((escolha == 1) and (maquina == 2)):
        print(f"Máquina: {computador}")
        print(f"{jogador}: {escolha_jogador}")
        print(f"\033[mA Máquina venceu!!\033[m")
    elif((escolha == 2) and (maquina == 3)):
        print(f"Máquina: {computador}")
        print(f"{jogador}: {escolha_jogador}")
        print(f"A Máquina venceu!!")
    elif((escolha == 3) and (maquina == 1)):
        print(f"Máquina: {computador}")
        print(f"{jogador}: {escolha_jogador}")
        print(f"A Máquina venceu!!")
    elif ((maquina == 1) and (escolha == 2)):
        print(f"Máquina: {computador}")
        print(f"{jogador}: {escolha_jogador}")
        print(f"\033[mVocê venceu!!\033[m")
        print(f"Winner!!")
    elif ((maquina == 2) and (escolha == 3)):
        print(f"Máquina: {computador}")
        print(f"{jogador}: {escolha_jogador}")
        print(f"\033[mVocê venceu!!\033[m")
        print(f"Winner!!")
    elif ((maquina == 3) and (escolha == 1)):
        print(f"Máquina: {computador}")
        print(f"{jogador}: {escolha_jogador}")
        print(f"\033[mVocê venceu!!\033[m")
        print(f"Winner!!")
















