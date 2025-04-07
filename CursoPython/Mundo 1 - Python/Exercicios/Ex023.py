#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Exercicio Aula 09

#Exemplo:
#Digite um número: 1834

#Unidade: 4
#Dezenas: 3
#Centena: 8
#Milhar: 1

numero = int(input("Digite um número: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar =  numero // 1000 % 10

print(f"Milhar: {milhar}")
print(f"Centena: {centena}")
print(f"Dezena: {dezena}")
print(f"Unidade: {unidade}")
