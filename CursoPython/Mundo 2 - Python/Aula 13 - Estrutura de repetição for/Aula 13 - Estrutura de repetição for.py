#Aula 13 - Estrutura de repetição for

inicio = int(input("Digite o inicio: "))

fim = int(input("Digite o final: "))

pulo = int(input("Digite o pulo: "))
for c in range(inicio, fim + 1, pulo):
    print(c)

print("Fim")

soma = 0

for c in range(1, 3):
    numero = int(input(f"Digite o {c}º número: "))
    soma += numero

print(f"O total da soma de todos os valores é {soma}")

