#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

import random

aluno_1 = input("1º aluno: ")
aluno_2 = input("2º aluno: ")
aluno_3 = input("3º aluno: ")
aluno_4 = input("4º aluno: ")

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
random.shuffle(alunos)
print(alunos)

