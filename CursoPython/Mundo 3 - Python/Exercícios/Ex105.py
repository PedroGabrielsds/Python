#Aula 21 - Funções (Parte 2)

#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
#com as seguintes informações:

#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

#Adicione também as DOCSTRINGS da função

def notas(* valores, situacao = False):
    """
    A função notas deverá receber quatro notas e mostrar as seguintes informações:
    #- Quantidade de notas
    #- A maior nota
    #- A menor nota
    #- A média da turma
    #- A situação (opcional)
    :param valores: Recebe as notas dos alunos
    :param situacao: Marca se vai ou não mostrar a situação em que a turma se encontra
    :return boletim: Retorna as informações das notas processadas
    """
    boletim = {}

    soma_notas = 0
    for nota in valores:
        soma_notas += nota

    boletim['Total'] = len(valores)
    boletim['maior'] = max(valores)
    boletim['menor'] = min(valores)
    boletim['media'] = soma_notas / len(valores)
    if(situacao == True):
        if(boletim['media'] >= 7):
            boletim['situacao'] = "Boa"
        elif(boletim['media'] >= 5):
            boletim['media'] = "Razoável"
        else:
            boletim['situacao'] = "Precária"
    print("---------------------------------")
    return boletim


estado = str(input(f"Deseja ver a situação da turma? [S/N] ")).upper().strip()[0]
while(estado not in "SN"):
    estado = str(input(f"Deseja ver a situação da turma? [S/N] ")).upper().strip()[0]

if (estado == "S"):
    estado = True
else:
    estado = False
# while(resposta != "N"):
#     dados.append(float(input(f"Digite a nota do aluno(a): ")))
#     resposta = "A"
#     while(resposta not in "SN"):
#         resposta = str(input(f"Deseja adicionar mais notas? [S/N] ")).strip().upper()[0]
#     if(resposta == "N"):
#         estado = "A"
#         while (estado not in "SN"):
#             estado = str(input(f"Deseja ver a situação da turma no boletim? [S/N] ")).upper().strip()[0]



resultado = notas(5, 6.5, 8, 9, situacao = estado)
print(resultado)
help(notas)