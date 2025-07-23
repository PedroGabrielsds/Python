#Aula 17 - Listas

#Crie um programa que vai ler vários números e colocar em uma lista.

#Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados, respectivamente.

#Ao final, mostre o conteúdo das três listas geradas.

pares = list()
impares = list()
numeros = list()
resposta =  's'

while(resposta != 'n'):
    valor = int(input(f"Digite um número: "))
    while(valor < 0):
        print(f"Número \033[1;31;40minválido\033[m! Tente novamente..")
        valor = int(input(f"Digite outro número: "))
    numeros.append(valor)
    resposta = str(input(f"Deseja digitar mais números? [S/N] ")).lower().strip()[0]

for numero in numeros:
    if(numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Esses foram os números que você digitou: {sorted(numeros)}")
print(f"Foram identificados esses {sorted(pares)} números pares na lista, ao todo são {len(pares)} números pares!")
print(f"Foram identificados esses {sorted(impares)} números ímpares na lista, ao todo são {len(impares)} números ímpares!")
