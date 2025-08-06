#Aula 18 - Listas Parte 2

#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

#A) Quantas pessoas foram cadastradas.

#B) Uma listagem com as pessoas mais pesadas.

#C) Uma listagem com as pessoas mais leves.

resposta = "S"
cadastros = []
pessoas = []

while(resposta != "N"):
    pessoas.append(str(input(f"Nome: ")))
    pessoas.append(float(input(f"Peso: ")))
    cadastros.append(pessoas[:])
    if(len(cadastros) == 1):
        maior_peso = pessoas[1]
        menor_peso = pessoas[1]
    elif(pessoas[1] >= maior_peso):
        maior_peso = pessoas[1]
    elif(pessoas[1] <= menor_peso):
        menor_peso = pessoas[1]

    pessoas.clear()

    resposta = str(input(f"Deseja cadastrar mais alguém? [S/N] ")).upper().strip()[0]
    while(resposta not in "NS"):
        resposta = str(input(f"Deseja cadastrar mais alguém? [S/N] ")).upper().strip()[0]

print("=-" * 30)

print(f"Foram feitos {len(cadastros)} cadastros!")
print(f"O maior peso registrado foi: {maior_peso}KG e é o peso de: ", end="")
for cadastro in cadastros:
    if(cadastro[1] == maior_peso):
        print(f"{cadastro[0]},", end=" ")

print()

print(f"O menor peso registrado foi: {menor_peso}KG e é o peso de: ", end="")
for cadastro in cadastros:
    if(cadastro[1] == menor_peso):
        print(f"{cadastro[0]},", end=" ")