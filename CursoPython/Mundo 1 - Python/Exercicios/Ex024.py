#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
#Exercicio Aula 09

nome_cidade = str(input("Digite o nome de uma cidade: ")).strip().lower()

nome_cidade_dividido = nome_cidade.split() [0]

print(f"{nome_cidade_dividido}")

print(f"É verdade que a cidade digitada começa com (Santo): {'santo' in nome_cidade_dividido}")


