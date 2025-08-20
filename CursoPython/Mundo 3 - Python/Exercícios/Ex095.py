#Aula 19 - Dicionários

#Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []
jogador = {}
gols = []
resposta = "S"

while resposta != "N":
    partidas = 0
    jogador['nome'] = str(input(f"Nome do Jogador: "))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    contador = 1
    while contador <= partidas:
        gols.append(int(input(f"Quantos gols na partida {contador}? ")))
        contador += 1

    jogador['gols'] = gols.copy()
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()

    resposta = str(input(f"Deseja continuar? [S/N] ")).upper().strip()[0]
    while resposta not in "NS":
        resposta = str(input(f"\033[1;31mOpção Incorreta\033[m! Deseja continuar? [S/N] ")).upper().strip()[0]
    print("-" * 20)

print(f"{f'Nome':>15}")
print(f"{f"Gols":>15}")
