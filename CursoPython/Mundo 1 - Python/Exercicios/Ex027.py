#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Exercicio Aula 09

#Exemplo: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

nome = str(input("Digite seu nome completo: ")).strip()


nome_dividido = nome.split()
print (len(nome_dividido))
print(f"Primeiro nome é: {nome_dividido [0]}")
print(f"Último nome é: {nome_dividido [len(nome_dividido) -1]}")

