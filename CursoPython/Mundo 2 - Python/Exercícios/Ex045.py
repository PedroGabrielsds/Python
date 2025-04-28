#Ex045

#Exercicio Aula 12 - Condições Aninhadas

#Crie um programa que faça o computador jogar jokenpô(Pedra, Papel e tesoura) com você.

import random

jogadas = ("Pedra", "Papel", "Tesoura")

computador = random.choice(jogadas)

print("\033[1;31;40m=--\033[m" * 5,"\033[1;37;40mPedra\033[m, Papel, Tesoura!", "\033[1;31;40m--=\033[m" * 5)

opcao = str(input("""[1] - Pedra 
[2] - Papel
[3] - Tesoura
Escolha sua jogada: """))










