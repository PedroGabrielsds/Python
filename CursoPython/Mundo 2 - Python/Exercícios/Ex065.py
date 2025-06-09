#Aula 14 - Estrutura de repetição While

#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
#valores e qual foi o maior e o menor valor lido.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta = "S"
contador = 1
qtd_numeros = 0
soma = 0

while(resposta != "N"):
    numero = int(input(f"Digite um o {contador}º número: "))
    if(numero > 0 and contador == 1):
        maior = numero
        menor = numero
    if(numero > maior):
        maior = numero
    if(numero < menor):
        menor = numero
    soma += numero
    media = float(soma / contador)
    resposta = str(input(f"Deseja digitar mais números: [S/N] ")).upper().strip()
    contador += 1
    qtd_numeros += 1

print(f"Você digitou {qtd_numeros} números e média foi {media:.2f}!")
print(f"O maior número foi {maior} e o menor foi {menor}")