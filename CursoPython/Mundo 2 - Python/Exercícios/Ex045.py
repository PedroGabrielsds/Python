#Ex045

#Exercicio Aula 12 - Condições Aninhadas

#Crie um programa que faça o computador jogar jokenpô(Pedra, Papel e tesoura) com você.

import random

import time

print("\033[1;31;40m=--\033[m" * 5,"JOKENPÔ", "\033[1;31;40m--=\033[m" * 5)

jogadas = ('Pedra', 'Papel', 'Tesoura')
maquina = random.randint(0, 2)

jogador = str(input("\033[1;33;40mQual seu nickname? \033[m"))

escolha = int(input("""\033[1;37;40m[0] - Pedra\033[m 
\033[1;38;40m[1] - Papel\033[m
\033[1;31;40m[2] - Tesoura\033[m
\033[1;33;40mEscolha sua jogada:\033[m """))

if(maquina == escolha):

    print(f"\033[1;38;40mMáquina:\033[m {jogadas[maquina]}")
    print(f"\033[1;36;40m{jogador}:\033[m {jogadas[escolha]}")
    print(f"\033[1;33;40mEmpate\033[m!! \033[1;37;40mTente novamente...\033[m")

else:

    print("\033[1;37;40mJo\033[m")
    time.sleep(1)
    print("\033[1;38;40mKen\033[m")
    time.sleep(1)
    print("\033[1;31;40mPô!\033[m")

    if(escolha == 0 and maquina == 2) or (escolha == 1 and maquina == 0) or (escolha == 2 and maquina == 1):

        print(f"\033[1;38;40mMáquina:\033[m {jogadas[maquina]}")
        print(f"\033[1;36;40m{jogador}:\033[m {jogadas[escolha]}")
        print(f"\033[1;32;40mWinner\033[m!!")
        print(f"\033[1;32;40mVocê ganhou, parabéns\033[m!!")

    else:

        print(f"\033[1;38;40mMáquina:\033[m {jogadas[maquina]}")
        print(f"\033[1;36;40m{jogador}:\033[m {jogadas[escolha]}")
        print(f"\033[1;31;40mLoser!!\033[m")
        print(f"\033[1;31;40mVocê perdeu\033[m!! \033[1;37;40mTente novamente...\033[m")