#Aula 20 - Funções (Parte 1):

#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: Inicio, Fim e Passo e realize a contagem.

#Seu programa deverá realizar três contagens através da função criada:

#A) De 1 até 10, de 1 em 1;
#B) De 10 até 0, de 2 em 2;
#C) Uma contagem personalizada.

from time import sleep

def linha():
    print('-' * 20)

def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if((inicio < fim) or (passo < 0)):
        for cont in range(inicio, fim + 1, passo):
            print(cont, end=" ")
            sleep(0.5)
        print(f"Fim")
    elif(inicio > fim):
        for cont in range(inicio, fim + 1, -passo):
            print(cont, end=" ")
            sleep(0.5)
        print(f"Fim")

#Programa Principal
inicio = 1
fim = 10
passo = 1
contador(inicio, fim, passo)

sleep(1)
linha()

inicio = 10
fim = 0
passo = 2
contador(inicio, fim, passo)

sleep(1)
linha()

print(f"Contador personalizado!")
inicio = int(input(f"Inicio: "))
fim = int(input(f"Fim: "))
passo = int(input(f"Passo: "))
linha()
contador(inicio, fim, passo)