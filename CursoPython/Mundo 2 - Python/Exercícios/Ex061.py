#Aula 14 - Estrutura de repetição While

#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
#usando a estrutura while:

resposta = 's'

while(resposta != 'n'):
    primeiro_termo = int(input(f"Digite o primeiro termo: "))
    razao = int(input(f"Qual é a razão? "))

    an = primeiro_termo + (10 - 1) * razao
    sn = (primeiro_termo + an) * 10 / 2
    qtd_termos = 0

    while(qtd_termos < 10):
        qtd_termos += 1
        print(f"{primeiro_termo} -->", end=" ")
        primeiro_termo += razao

    print("Acabou!")
    resposta = str(input(f"Deseja realizar outra Progressão Aritmética? [S/N]")).lower().strip()