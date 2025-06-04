#Ex055 - Aula 13

#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido!

maior_peso = 0
menor_peso = 0

for contador in range(1, 6):
    peso = float(input(f"Peso da {contador} pessoa: Kg"))
    if(maior_peso == 0):
        maior_peso = peso
        menor_peso = peso
    else:
        if(peso > maior_peso):
            maior_peso = peso

        elif(peso < menor_peso):
            menor_peso = peso

print(f"O maior peso foi {maior_peso}Kg")
print(f"O menor peso foi {menor_peso}Kg")