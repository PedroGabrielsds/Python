#Aula 15 - Interrompendo repetições while

#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai para quando o usuário digitar o valor 999,
#Que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

numero = 0
soma = 0
contador = 0

while(numero != 999):
    numero = int(input(f"Digite o {contador + 1}º número: (999 para parar) "))
    if(numero == 999):
        break
    else:
        soma += numero
        contador += 1

print(f"A soma de {contador} números resultou em {soma}")