#Aula 14 - Estrutura de repetição While

#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
#usando a estrutura while:

primeiro_termo = int(input(f"Digite o primeiro termo: "))
razao = int(input(f"Qual é a razão? "))

an = primeiro_termo + (10 - 1) * razao
sn = (primeiro_termo + an) * 10 / 2

