#Aula 19 - Dicionários

#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
#No final, coloque esses dicionários em ordem. Sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint
from operator import itemgetter

jogadores = []
jogadas = {}
ranking = []
contador = 1

while contador <= 4:
    jogadas[(f'jogador{contador}')] = randint(1, 6)
    contador += 1

print(f"Valores Sorteados: ")

for key, value in jogadas.items():
    print(f"{f"O {key} tirou {value} no dado!"}")
    sleep(1)

print("-=" * 17)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print(f"{'== Ranking Dos Jogadores ==':^33}")
for contador in range(0, len(jogadas)):
    print(f"{f"{contador + 1}º Lugar: {ranking[contador][0]} com {ranking[contador][1]}":^33}")
    sleep(1)