#Aula 19 - Dicionários

#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
#partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário.
#incluindo o total de gols feitos durante o campeonato.

informacoes = {}
gols = []
total = 0

informacoes['nome'] = str(input(f"Nome do jogador: "))
partidas = int(input(f"Quantas partidas {informacoes['nome']} jogou? "))
contador = 1
while contador <= partidas:
    valor = int(input(f"Quantos gols {informacoes['nome']} fez na partida {contador}? "))
    gols.append(valor)
    contador += 1
    total += valor

informacoes['gols'] = gols
informacoes['total'] = total

print("-=" * 30)
print(informacoes)
print("=-" * 30)
for key, value in informacoes.items():
    print(f"O campo {key} tem o valor {value}.")

print("-=" * 30)
print(f"O jogador {informacoes['nome']} jogou {partidas} partidas.")
contador = 1
for partida in gols:
    print(f"{f"=> Na partida {contador}, fez {partida}":>25}", end=" ")
    if(partida > 1):
        print(f"gols.")
    else:
        print(f"gol.")
    contador += 1