#Aula 18 - Listas Parte 2

#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

#A) Quantas pessoas foram cadastradas.

#B) Uma listagem com as pessoas mais pesadas.

#C) Uma listagem com as pessoas mais leves.

resposta = "S"
qtd_cadastros = 0
cadastros = []
pessoas = []


while(resposta != "N"):
    qtd_cadastros += 1
    # if(qtd_cadastros == 1):
    #     pesado = peso
    #     leve = peso
    # elif(peso >= pesado):
    #     pesado = peso
    # elif(peso <= leve):
    #     leve = peso
    pessoas.append(str(input(f"Nome: ")))
    pessoas.append(float(input(f"Peso: ")))
    cadastros.append(pessoas[:])
    pessoas.clear()

    resposta = str(input(f"Deseja cadastrar mais alguém? ")).upper().split()[0]
    while(resposta not in "NS"):
        resposta = str(input(f"Deseja cadastrar mais alguém? ")).upper().split()[0]
        if (resposta == "N"):
            break



print(cadastros)
print(cadastros[0])
print(cadastros[0][1])

for posicao, pessoa in enumerate(cadastros):
    if(posicao == 0):
        maior_peso = pessoa[1]
        menor_peso = pessoa[1]
    elif(pessoa[1] >= maior_peso):
        maior_peso = pessoa[1]
    elif(pessoa[1] <= menor_peso):
        menor_peso = pessoa[1]


    print(f"A pessoas mais pesadas pesam {maior_peso} e são: {}")