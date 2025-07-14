#Aula 17 - Listas

#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

#No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.

contador = 1
maior_valor = 0
menor_valor = 0
plural = False
numeros = list()

while(len(numeros) < 5):
    numeros.append(int(input(f"Digite o {contador}º valor: ")))
    contador += 1

print(f"=-" * 30)

contador = 0
for posicao, valor in enumerate(numeros):
    if(valor == max(numeros)):
        contador += 1
        if(contador > 1):
            plural = True
        if(valor == max(numeros) and contador == 1):
            if(plural == True):
                print(f"O MAIOR valor digitado foi {max(numeros)} localizado nas posições: {posicao + 1}", end="")
            else:
                print(f"O MAIOR valor digitado foi {max(numeros)} localizado na posição: {posicao + 1}", end="")
        elif(valor == max(numeros) and (contador > 1)):
            print(f", {posicao + 1}", end="")

print("")
plural = False
contador = 0
for posicao, valor in enumerate(numeros):
    if(valor == min(numeros)):
        contador += 1
        if(contador > 1):
            plural = True
        if((valor == min(numeros)) and (contador == 1)):
            if(plural == True):
                print(f"O MENOR valor digitado foi {min(numeros)} localizado nas posições: {posicao + 1}", end="")
            else:
                print(f"O MENOR valor digitado foi {min(numeros)} localizado na posição: {posicao + 1}", end="")
        elif(valor == min(numeros) and contador > 1):
            print(f", {posicao + 1}")

#Análisar como fazer funcionar o plural e como diminuir código de verificação para maior e menor - Nota 14/07/2025