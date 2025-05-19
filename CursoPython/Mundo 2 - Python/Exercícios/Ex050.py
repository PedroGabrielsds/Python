#Ex050 - Aula 13

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o
soma_pares = 0

for contador in range(1, 7):
    numero = int(input(f"Digite o {contador}º número: "))
    if (numero % 2 == 0):
        soma_pares += numero

print(f"A soma de todos os números pares resultou em: {soma_pares}")
