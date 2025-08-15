#Aula 19 - Dicionários

#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
#No final, coloque esses dicionários em ordem. Sabendo que o vencedor tirou o maior número no dado.

from random import randint

jogadores = []
jogadas = {}
ranking = {}
for contador in range(1, 5):
    jogadas[f'jogador{contador}'] = randint(1, 6)
    jogadores.append(jogadas.copy())
    jogadas.clear()

print(jogadores)

for posicao, jogador in enumerate(jogadores):
    for jogada in jogadas:
        print(jogador)
        # if(posicao == 0):
        #     maior = menor = jogadas
        # else:
        #     if(value > maior):
        #         ranking.insert(posicao, jogador)
        #     #elif(value < menor):
        #         ranking.insert(posicao, jogador)