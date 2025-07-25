#Aula 17 - Listas

#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

#No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.

contador = 1
singular = "na posição"
plural = "nas posições"
numeros = list()
posicoes_max = list()
posicoes_min = list()

while(len(numeros) < 5):
    numeros.append(int(input(f"Digite o {contador}º valor: ")))
    contador += 1

print(f"=-" * 30)

for posicao, valor in enumerate(numeros):
    if(valor == max(numeros)):
        posicoes_max.append(posicao + 1)
    elif(valor == min(numeros)):
        posicoes_min.append(posicao + 1)

print(f"Você digitou os valores {numeros}")
if(len(posicoes_max) > 1):
    print(f"O maior valor digitado foi: \033[1;37m{max(numeros)}\033[m {plural}: {", ".join(map(str, posicoes_max))}")
elif(len(posicoes_max) == 1):
    print(f"O maior valor digitado foi: \033[1;37m{max(numeros)}\033[m {singular}: {", ".join(map(str, posicoes_max))}")

if(len(posicoes_min) > 1):
    print(f"O menor valor digitado foi: \033[1;37m{min(numeros)}\033[m {plural}: {", ".join(map(str, posicoes_min))}")
elif(len(posicoes_min) == 1):
    print(f"O menor valor digitado foi: \033[1;37m{min(numeros)}\033[m {singular}: {", ".join(map(str, posicoes_min))}")

#Primeira tentativa:
# for posicao, valor in enumerate(numeros):
#     if(posicao == 0 and valor == max(numeros)):
#         if(valor == max(numeros)):
#             contador_max += 1
#             if(contador_max > 1):
#                 plural = True
#             if(valor == max(numeros) and contador_max == 1):
#                 if(plural == True):
#                     print(f"O MAIOR valor digitado foi {max(numeros)} localizado nas posições: {posicao + 1}", end="")
#                 else:
#                     print(f"O MAIOR valor digitado foi {max(numeros)} localizado na posição: {posicao + 1}", end="")
#             elif(valor == max(numeros) and (contador_max > 1)):
#                 print(f", \033[1;32m{posicao + 1}", end="")
#         elif(valor == min(numeros)):
#             plural = False
#             for posicao, valor in enumerate(numeros):
#                 if(valor == min(numeros)):
#                     contador_min += 1
#                     if(contador_min > 1):
#                         plural = True
#                     if((valor == min(numeros)) and (contador_min == 1)):
#                         if(plural == True):
#                             print(f"O MENOR valor digitado foi {min(numeros)} localizado nas posições: {posicao + 1}", end="")
#                         else:
#                             print(f"O MENOR valor digitado foi {min(numeros)} localizado na posição: {posicao + 1}", end="")
#                     elif(valor == min(numeros) and contador_min > 1):
#                         print(f", \033[1;31m{posicao + 1}")