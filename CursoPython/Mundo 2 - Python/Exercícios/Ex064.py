#Aula 14 - Estrutura de repetição While

#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag (999)):

numero = 0
qtd_numeros = 0
soma = 0

while(numero != 999):
    numero = int(input(f"Digite um número: "))
    if(numero != 999):
        qtd_numeros += 1
        soma += numero

print(f"Você digitou {qtd_numeros} e a soma entre eles resultou em {soma}")