#Aula 19 - Dicionários

#Faça um programa que leia nome e média de um aluno, guardando também situação em um dicionário (Aprovado com média acima de 7).
#No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['Nome'] = str(input(f"Nome do aluno(a): "))
aluno['Média'] = float(input(f"Média do aluno(a) {aluno['Nome']}: "))
if(aluno['Média'] >= 7):
    aluno['Situação'] = "\033[1;32mAprovado\033[m"
else:
    aluno['Situação'] = "\033[1;31mReprovado\033[m"

print(f"-=" * 16)
contador = 0
for key, value in aluno.items():
    contador += 1
    if(contador == 1):
        print(f"{f"< Boletim do aluno(a) \033[1m{value}\033[m >":=^40}")
    elif(contador == 2):
        print(f"A {key} do aluno(a) \033[1m{aluno['Nome']}\033[m é \033[1m{value}\033[m")
    elif(contador == 3):
        print(f"A {key} do aluno(a) \033[1m{aluno['Nome']}\033 é {value}")