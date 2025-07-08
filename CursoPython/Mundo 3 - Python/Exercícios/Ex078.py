#Aula 17 - Listas

#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

#No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.

contador = 1
maior_valor = 0
menor_valor = 0
numeros = list()

while(len(numeros) < 5):
    numeros.append(int(input(f"Digite o {contador}º valor: ")))
    contador += 1

print(f"=-" * 30)

for posicao, valor in enumerate(numeros):
    if(valor == max(numeros)):
        if(maior_valor >= 1):
            print(end=f", {posicao}")
        else:
            print(f"\nO maior valor digitado foi {max(numeros)} localizado na posição: {posicao + 1}", end=" ")
        maior_valor += 1
    if(valor == min(numeros)):
        if(menor_valor >= 1):
            print(end=f", {posicao}")
        else:
            print(f"\nO menor valor digitado foi {min(numeros)} localizado na posição: {posicao + 1}", end=" ")
        menor_valor += 1