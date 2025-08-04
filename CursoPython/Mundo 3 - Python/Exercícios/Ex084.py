#Aula 18 - Listas Parte 2

#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

#A) Quantas pessoas foram cadastradas.

#B) Uma listagem com as pessoas mais pesadas.

#C) Uma listagem com as pessoas mais leves.

resposta = "S"
qtd_cadastros = 0

while(resposta != "N"):
    qtd_cadastros += 1
    nome = str(input(f"Nome: "))
    peso = float(input(f"Peso: "))
    if(qtd_cadastros == 1):
        pesado = peso
        leve = peso
    elif(peso >= pesado):
        pesado = peso
    elif(peso <= leve):
        leve = peso

    resposta = str(input(f"Deseja cadastrar mais alguém? ")).upper().split()[0]
    while(resposta not in "NS"):
        resposta = str(input(f"Deseja cadastrar mais alguém? ")).upper().split()[0]

    if(resposta == "N"):
        break

print(f"O maior peso registrado é: {pesado}")
print(f"O menor peso registrado é: {leve}")