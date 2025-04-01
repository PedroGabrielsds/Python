#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

nome_cidade = input("Digite o nome de uma cidade: ")

nome_cidade_dividido = nome_cidade.split() [0]

print("É verdade que a cidade digitada começa com (Santo): ", ('Santo' in nome_cidade_dividido))