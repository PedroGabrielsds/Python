#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deels e escrevendo o nome escolhido.

import random

aluno_1 = input("1º aluno(a): ")
aluno_2 = input("2º aluno(a): ")
aluno_3 = input("3º aluno(a): ")
aluno_4 = input("4º aluno(a): ")

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

aluno_escolhido = random.choice(alunos)

print(f"O aluno(a) escolhido foi: {aluno_escolhido}")

