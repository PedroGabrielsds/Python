#Ex056 - Aula 13

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo;
#Qual é o nome do homem mais velho;
#Quantas mulheres têm menos de 20 anos.

mais_velho = ""
maior_idade = 0
mulheres_menores_idade = 0
total_idades = 0

for contador in range(1, 5):
    print(f"\033[1;{30 + contador};40m======|{contador}º Pessoa|======\033[m")
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo (M/F): ")).strip().lower()
    total_idades += idade

    if((idade > maior_idade) and (sexo == "masculino") or (sexo == 'm')):
        mais_velho = nome
        maior_idade = idade

    else:
        if((sexo == "feminino") or (sexo == 'f') and (idade < 20)):
            mulheres_menores_idade += 1

media_idades = total_idades / 4
print(f"A média de idade deste grupo é de {media_idades} anos")
print(f"O Homem mais velho tem {maior_idade} e se chama {mais_velho}")
print(f"{mulheres_menores_idade} mulheres são menores de idade!")