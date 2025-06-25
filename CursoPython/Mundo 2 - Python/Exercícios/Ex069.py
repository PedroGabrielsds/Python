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
qtd_mulheres_menores = 0
sexo = ""
nome = ""
idade = 0

while(resposta != "N"):
    qtd_pessoas += 1
    print(f"{'Cadastramento':=^40}")
    nome = str(input(f"Nome: ")).lower().strip()
    idade = int(input(f"Idade: "))
    sexo = str(input(f"Sexo: [M/F]")).upper().strip()[0]
    while(sexo != 'M' and sexo != 'F'):
        sexo = str(input(f"Sexo: [M/F]")).upper().strip()[0]

    if (idade >= 18):
        maior_dezoito += 1
        unico_maior = nome

    if (sexo == "M"):
        qtd_homens += 1
        unico_homem = nome

    if (sexo == "F" and idade < 20):
        qtd_mulheres_menores += 1
        unica_mulher_menor = nome

    resposta = str(input(f"Deseja cadastrar mais pessoas? [S/N]")).upper().strip()[0]
    while(resposta != "S" and resposta != "N"):
        print(f"Opção \033[1;31minválida\033[m, tente novamente!")
        resposta = str(input(f"Deseja cadastrar mais pessoas? [S/N]")).upper().strip()[0]

print("=" * 40)
if(qtd_homens > 1):
    print(f"{qtd_homens} Homens foram cadastrados!")
elif(qtd_homens == 0):
    print("Nenhum Homem foi cadastrado!")
else:
    print(f"Somente 1 Homem foi cadastrado e se chama {unico_homem}")

if(maior_dezoito > 1):
    print(f"{maior_dezoito} são maiores de 18 anos!")
elif(maior_dezoito == 0):
    print(f"Nenhuma pessoa cadastrada é maior de dezoito!")
else:
    print(f"Apenas 1 pessoa contém 18 anos ou mais e se chama {unico_maior}")

if(qtd_mulheres_menores > 1):
    print(f"{qtd_mulheres_menores} mulheres são menores de 20 anos de idade!")
elif(qtd_mulheres_menores == 0):
    print(f"Nenhuma mulher menor de 20 anos foi cadastrada!")
else:
    print(f"Apenas 1 mulher menor de 20 anos foi cadastrada e se chama {unica_mulher_menor}!")