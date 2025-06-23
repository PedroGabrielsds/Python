#Aula 15 - Interrompendo repetições while

#crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer
#continuar. No final, mostre:

#A) Quantas pessoas tem mais de 18 anos;
#B) Quantos homens foram cadastrados;
#C) Quantas mulheres tem menos de 20 anos.

resposta = "S"
qtd_pessoas = 0
maior_dezoito = 0
qtd_homens = 0
sexo = ""
nome = ""
idade = 0

while(resposta != "N"):
    qtd_pessoas += 1
    print(f"Cadastro: ")
    nome = str(input(f"Nome: ")).lower().strip()
    idade = int(input(f"Idade: "))
    sexo = str(input(f"Sexo: [M/F]")).lower().strip()
    while(sexo != "mf"):
        sexo = str(input(f"Sexo: [M/F]")).lower().strip()
    if(idade >= 18):
        maior_dezoito += 1

    if(sexo == "m"):
        qtd_homens += 1

    if():

print(f"{maior_dezoito} pessoas são maiores ou tem 18 anos!")
if(qtd_homens > 1):
    print(f"{} Homens foram cadastrados!")
else:
    print(f"Somente 1 Homem foi cadastrado e se chama {}")