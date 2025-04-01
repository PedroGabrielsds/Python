#Crie um programa que leia o nome completo de uma pessoa e mostre:

#-> O nome com todas as letras maiúsculas;
#-> O nome com todas minúsculas;
#-> Quantas letras ao todo (sem considerar espaços);
#-> Quantas letras tem o primeiro nome.

nome = input("Seu nome completo: ")

print(nome.upper())
print(nome.lower())
print(len(nome.strip()))
nome_dividido = nome.split()
print(len(nome_dividido [0]))