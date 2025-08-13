#Aula 18 - Listas Parte 2

#Crie um programa que leia nome e duas notas de vários alunos e guarde de tudo em uma lista composta. No final,
#mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from time import sleep

boletim = []
auxiliar = []
alunos = []
resposta = "S"

while resposta != "N":
    auxiliar.append(str(input(f"Nome: ")))
    auxiliar.append(float(input(f"Nota 1: ")))
    auxiliar.append(float(input(f"Nota 2: ")))
    boletim.append(auxiliar[:])
    resposta = str(input(f"Deseja continuar? [S/N] ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input(f"Deseja continuar? [S/N] ")).strip().upper()[0]

    auxiliar.clear()

print("=-" * 40)
print(f"{f"Nº":<4}", end="")
print(f"{f"NOME":<20}", end="")
print(f"MÉDIA")

print(f"-" * 30)
for posicao, aluno in enumerate(boletim):
    alunos.append(posicao)
    media = (aluno[1] + aluno[2]) / 2
    print(f"{f"\033[1m{posicao}\033[m":<4}", end="")
    print(f"{f"\033[1m{aluno[0]}\033[m":<20}", end="")
    print(f"\033[1m{media:.2f}\033[m")

print("-" * 30)
aluno = int(input(f"Deseja ver a nota de qual aluno(a)? (999 interrompe!) "))
while aluno != 999:
    if(aluno not in alunos):
        print(f"\033[1;31mAluno inexistente\033[m, tente novamente!")
        aluno = int(input(f"Deseja ver a nota de qual aluno(a)? (999 interrompe!) "))
    else:
        print(f"Notas de \033[1m{boletim[aluno][0]}\033[m são \033[m{boletim[aluno][1]}\033[m, \033[1m{boletim[aluno][2]}\033[m")
        print("-" * 35)
        aluno = int(input(f"Deseja ver a nota de qual aluno(a)? (999 interrompe!) "))

print(F"\033[1;31mFinalizando boletim\033[m", end="")
contador = 0
while(contador < 3):
    if(contador == 3):
        print(f"\033[1;31m.\033[m")
    else:
        print("\033[1;31m.\033[m", end="")
        sleep(1)
        contador += 1