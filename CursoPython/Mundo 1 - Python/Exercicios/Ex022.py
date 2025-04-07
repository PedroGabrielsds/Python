#Crie um programa que leia o nome completo de uma pessoa e mostre:
#Exercicio Aula 09

#-> O nome com todas as letras maiúsculas;
#-> O nome com todas minúsculas;
#-> Quantas letras ao todo (sem considerar espaços);
#-> Quantas letras tem o primeiro nome.

nome = str(input("Seu nome completo: ")).strip()

print("Seu nome todo maiúsculo:", nome.upper())
print("Seu nome todo minúsculo: ", nome.lower())
print(nome.strip())
print("Seu nome ao todo contém:",len(nome) - nome.count(' '), "letras!")
nome_dividido = nome.split()
print("Seu primeiro nome é ", nome_dividido [0], "e tem ",len(nome_dividido [0]), "letras")

