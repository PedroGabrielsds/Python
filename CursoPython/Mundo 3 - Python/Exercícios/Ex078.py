#Aula 17 - Listas

#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

#No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.

contador = 1
numeros = list()
while(len(numeros) < 5):
    numeros.append(int(input(f"Digite o {contador}º valor: ")))
    contador += 1

for posicao, valor in enumerate(numeros):
    if(valor == max(numeros)):
        print(f"O maior valor digitado foi {max(numeros)} localizado na posição: {posicao + 1}")
    elif(valor == min(numeros)):
        print(f"O menor valor digitado foi {min(numeros)} localizado na posição: {posicao + 1}")