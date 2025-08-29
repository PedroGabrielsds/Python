#Aula 21 - Funções (Parte 2)

#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha de jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<Desconhecido>', gols = 0):
    """
    Função responsável por mostrar o nome e gol(s) de um jogador passado pelo usuário!
    :param nome: Coleta o nome do jogador!
    :param gols: Coleta a quantidade de gol(s) do jogador no campeonato!
    :return: Sem retorno
    Função Criada Por Mack
    """
    if(gols == 1):
        print(f"O jogador \033[1m{nome}\033[m fez apenas \033[1m{gols}\033[m gol no campeonato!")
    elif(gols > 1):
        print(f"O jogador \033[1m{nome}\033[m fez \033[1m{gols}\033[m gols no campeonato!")
    elif(gols == 0):
        print(f"O jogador \033[1m{nome}\033[m não fez nenhum gol no campeonato!")

#Programa Principal:
print('--' * 20)
nome = str(input(f"Nome do jogador: "))
gols = input(f"Número de Gols: ")
ficha(nome, gols)
help(ficha)