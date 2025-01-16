#Faça um programa que leia um número inteiro e mostre o seu sucessor e seu antecessor:

numero = int(input("Digite um número e descubra o seu antecessor e sucessor: "))
antecessor = int(numero - 1)
sucessor = int(numero + 1)

print(f"Antecessor: {numero - 1}, número digitado: {numero}, sucessor: {numero + 1}")
