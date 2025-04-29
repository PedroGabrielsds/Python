#Ex045

#Exercicio Aula 12 - Condições Aninhadas

#Crie um programa que faça o computador jogar jokenpô(Pedra, Papel e tesoura) com você.

import random

print("\033[1;31;40m=--\033[m" * 5,"JOKENPÔ", "\033[1;31;40m--=\033[m" * 5)

jogador = str(input("Qual seu nickname? "))

opcao = int(input("""\033[1;37;40m[1] - Pedra\033[m 
\033[1;38;40m[2] - Papel\033[m
\033[1;31;40m[3] - Tesoura\033[m
\033[1;33;40mEscolha sua jogada:\033[m """))

if((opcao != 1) and (opcao != 2) and (opcao != 3)):
    print("Opção inválida tente novamente...")
else:
    print("Jo")
    print("Ken")
    print("Pô!")

    jogadas = ("Pedra", "Papel", "Tesoura")
    computador = random.choice(jogadas)

    if():
        print(f"Computador: {computador}")
        print(f"{jogador}: Papel")
        print(f"Empate!! Tente novamente...")
    else:
        if(() and ()):
            print(f"Computador: {computador}")
            print(f"{jogador}: Tesoura")
            print("O computador ganhou, tente mais uma vez!")

        elif(() and ()):
            print(f"Computador: {computador}")
            print(f"{jogador}: Papel")
            print("O computador ganhou, tente mais uma vez!")

        elif(() and ()):
            print(f"Computador: {computador}")
            print(f"{jogador}: Pedra")
            print(f"O computador ganhou, tente mais uma vez!")

        elif(() and ()):
            print(f"Computador: {computador}")
            print(f"{jogador}: Tesoura")
            print(f"Winner!!")
            print("Vencedor!")

        elif(() and ()):
            print(f"Computador: {computador}")
            print(f"{jogador}: Papel")
            print(f"Winner!!")
            print("Vencedor!")

        elif(() and ()):
            print(f"Computador: {computador}")
            print(f"{jogador}: Pedra")
            print(f"Winner!!")
            print("Vencedor!")











