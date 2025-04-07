#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
#Exercicio Aula 09

nome = str(input("Digite seu nome completo: ")).strip().lower()

print(f"Existe (Silva) no seu nome: {'silva' in nome}")