#Aula 14 - Estrutura de repetição While

#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta = "S"
contador = 1
soma = 0

while(resposta != "N"):
    numero = int(input(f"Digite um o {contador}º número: "))
    resposta = str(input(f"Deseja digitar mais números: [S/N] ")).upper().strip()
    soma += numero
    media = float(soma / contador)
    contador += 1

print(f"A média de {soma} é {media:.2f}!")