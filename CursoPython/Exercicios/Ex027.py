#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

#Exemplo: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

nome = input("Digite seu nome completo: ")

print("Primeiro nome: ", nome.split() [0])
nome_dividido = nome.split()
print("Último nome: ", nome_dividido[4])