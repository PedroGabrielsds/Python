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
        elif(boletim['media'] == 6.5):
            boletim['media'] = "Razoável"
        else:
            boletim['situacao'] = "Precária"
    print("---------------------------------")
    return boletim


resultado = notas(5.5, 6, 9.5, 7.2, situacao = True)
print(resultado)

help(notas)