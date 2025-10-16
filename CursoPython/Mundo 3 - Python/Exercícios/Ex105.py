#Aula 21 - Funções (Parte 2)

#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
#com as seguintes informações:

#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

#Adicione também as DOCSTRINGS da função

def notas(* notas):
    """
    A função notas deverá receber quatro notas e mostrar as seguintes informações:
    #- Quantidade de notas
    #- A maior nota
    #- A menor nota
    #- A média da turma
    #- A situação (opcional)
    :param notas: Recebe uma lista de quatro notas.
    :return: Retorna o boletim com as informações citadas a cima.
    """
    boletim = []
    soma_notas = 0

    soma_notas += notas

    boletim['total'] = len(notas)
    boletim['maior'] = max(notas)
    boletim['menor'] = min(notas)

    media = soma_notas / len(notas)
    boletim['media'] = media

    return boletim


#Programa Principal
resultado = notas(5.5, 9.5, 10, 6.5)
print(resultado)