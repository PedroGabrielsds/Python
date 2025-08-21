#Aula 19 - Dicionários

#Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

from time import sleep

jogadores = []
jogador = {}
gols = []
posicoes = []
resposta = "S"

while resposta != "N":
    total = 0
    partidas = 0
    jogador['nome'] = str(input(f"Nome do Jogador: "))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    contador = 1
    while contador <= partidas:
        gol = (int(input(f"Quantos gols na partida {contador}? ")))
        contador += 1
        gols.append(gol)
        total += gol
    jogador['gols'] = gols[:]
    jogador['total'] = total
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()

    resposta = str(input(f"Deseja continuar? [S/N] ")).upper().strip()[0]
    while resposta not in "NS":
        resposta = str(input(f"\033[1;31mOpção Incorreta\033[m! Deseja continuar? [S/N] ")).upper().strip()[0]
    print("--" * 25)

print(f"{f"Código":<10}", end="")
print(f"{f'Nome':<15}", end="")
print(f"{f"Gols"}", end="")
print(f"{f"Total":>20}")
print(f"--" * 25)

for posicao, player in enumerate(jogadores):
        posicoes.append(posicao+1)
        print(f"{posicao+1:<10}", end="")
        print(f"{player['nome']:<15}", end="")
        print(f"{player['gols']}", end="")
        print(f"{player['total']:>14}")

dado = int(input(f"Mostrar dados de qual jogador? (999 termina)"))
while(dado != 999):
    if dado not in posicoes:
        print(f"\033[1;31mERRO\033[m! \033[1;33mNão existe jogador com código {dado}\033[m! Tente novamente!")
    else:
        print(f"-- Levantamento do jogador {jogadores[dado-1]['nome']}:")
        for gol in range(0, len(jogadores[dado-1]['gols'])):
            print(f"{f"No jogo {gol} fez {jogadores[dado-1]['gols'][gol]} gols.":>24}")
    print("--" * 25)
    dado = int(input(f"Mostrar dados de qual jogador? (999 termina)"))

print("<< Finalizando", end="")
for contador in range(1, 3 + 1):
    if(contador < 3):
        print(f"\033[1m.\033[m", end="")
        sleep(1)
    else:
        print(f"\033[1m.\033[m >>")