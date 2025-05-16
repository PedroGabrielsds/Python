#Ex048 - Aula 13

#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplo de três e que
#se encontram no intervalo de 1 até 500
impares = 0
qtd_impares = 0
qtd_multiplo_tres = 0
soma_impares = 0

for contador in range(1, 500):
    if((contador % 2 == 1) and (contador % 3 == 0)):
        impares = contador
        qtd_impares += 1
        soma_impares = soma_impares + impares
        qtd_multiplo_tres += 1

print(f"No intervalo de 1 - 500, contém {qtd_impares} número ímpares!")
print(f"De {qtd_impares} números ímpares, {qtd_multiplo_tres} são múltiplos de 3!")
print(f"A soma de todos os número ímpares no intervalo de 1 até 500 é: {soma_impares}")


