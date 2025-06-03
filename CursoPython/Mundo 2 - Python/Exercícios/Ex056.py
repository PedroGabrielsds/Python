#Ex056 - Aula 13

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo;
#Qual é o nome do homem mais velho;
#Quantas mulheres têm menos de 20 anos.

mais_velho = 0
mulheres_menores_idade = 0
total_idades = 0

for contador in range(1, 5):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo (Masculino/Feminino): ")).lower()


    total_idades += idade

    if((idade > mais_velho) and (sexo == "masculino")):
        mais_velho = nome
        maior_idade = idade

    else:
        if((sexo == "feminino") and (idade < 20)):
            mulheres_menores_idade += 1

media_idades = total_idades  / 4
