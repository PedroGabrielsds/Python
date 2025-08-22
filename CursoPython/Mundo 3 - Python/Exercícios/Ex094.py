#Aula 19 - Dicionários

#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
#os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade do grupo.
#C) Uma lista com todas as mulheres.
#D) Uma lista com todas as pessoas com idade acima da média

#ADICIONAR TRATAMENTO DE ERRO PARA DIFERENTES TIPOS DE SEXO!!!!

grupo = []
pessoa = {}
acima_media = []
mulheres = []
resposta = 'S'
idades = 0
cadastros = 0

while resposta != "N":
    cadastros += 1
    pessoa['nome'] = str(input(f"Nome: ")).strip().title()
    pessoa['sexo'] = str(input(f"Sexo [M/F]: ")).upper().strip()[0]
    while(pessoa['sexo'] not in "MF"):
        print(f"Erro! Por favor, digite apenas M ou F.")
        pessoa['sexo'] = str(input(f"Sexo [M/F]: "))
    pessoa['idade'] = int(input(f"Idade: "))
    idades += pessoa['idade']
    if(pessoa['sexo'] == "F"):
        mulheres.append(pessoa['nome'])
    grupo.append(pessoa.copy())
    pessoa.clear()

    resposta = str(input(f"Deseja continuar [S/N]: ")).upper().strip()[0]
    while resposta not in "SN":
        print(f"Erro! Por favor, digite apenas S ou N.")
        resposta = str(input(f"Deseja continuar [S/N]: ")).upper().strip()[0]

media = idades / len(grupo)

print("-=" * 20)
print(f"- O grupo tem {cadastros} pessoas")
print(f"- A média de idade é de: {media}")
print(f"- As mulheres cadastradas foram: ", end="")
for posicao, mulher in enumerate(mulheres):
    if(posicao + 1 == len(mulheres)):
        print(f"{mulher}")
    else:
        print(f"{mulher}, ", end="")

print(f"- Lista de pessoas que estão acima da média:")
for posicao, pessoa in enumerate(grupo):
     if(pessoa['idade'] > media):
         print(f"Nome: {pessoa['nome']}; sexo = {pessoa['sexo']}; idade = {pessoa['idade']}; \n")

print("<< ENCERRADO >>")