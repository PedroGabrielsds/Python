#Aula 18 - Listas Parte 2

#Crie um programa que leia nome e duas notas de vários alunos e guarde de tudo em uma lista composta. No final,
#mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
auxiliar = []
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
    media = (aluno[1] + aluno[2]) / 2
    print(f"{f"{posicao}":<4}", end="")
    print(f"{f"{aluno[0]}":<20}", end="")
    print(f"{media}")

print("-" * 30)
aluno = int(input(F"Nota de qual aluno deseja ver? "))
while aluno != 999:
    
