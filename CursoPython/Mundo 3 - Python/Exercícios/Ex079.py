#Aula 17 - Listas

#Crie um programa no qual o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número
#já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()
numeros_repetidos = list()
resposta = "s"

while(resposta != "n"):
    valor = int(input(f"Digite um número: "))
    if(valor not in numeros):
        numeros.append(valor)
        print(f"Número aceito, foi considerado!")

    else:
        print(f"O valor já foi digitado, será desconsiderado!")
        numeros_repetidos.append(valor)
        while(valor in numeros_repetidos):
            valor = int(input(f"Digite outro número: "))
        print(f"Número aceito, foi considerado!")
        numeros.append(valor)

    resposta = str(input(f"Deseja digitar mais um número: [S/N] ")).lower().strip()
    while(resposta not in 'ns'):
        print(f"\033[1;31mOpção inválida\033[m!")
        resposta = str(input(f"Deseja digitar mais um número: [S/N] ")).lower().strip()

print(f"Esses são os números que foram digitados {sorted(numeros)}")