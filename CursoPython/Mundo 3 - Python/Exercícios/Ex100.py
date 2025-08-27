#Aula 20 - Funções (Parte 1):

#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
#todos os valores Pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(valores):
    while len(valores) <= 5:
        valores.append(randint(1, 10))
    print(f"Sorteando 5 valores da lista: ", end="")
    for valor in valores:
        sleep(0.3)
        print(valor, end=" ")
    print(f"Pronto!")

def pares(valores):
    soma_pares = 0
    print(f"Os valores pares são: ", end="")
    for valor in valores:
        if(valor % 2 == 0):
            print(valor, end=" ")
            if (valor % 2 == 0):
                soma_pares += valor
    print(f"e somados resultam em: {soma_pares}")

#Programa Principal
valores = []
sorteia(valores)
pares(valores)