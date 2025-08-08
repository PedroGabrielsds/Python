#Aula 18 - Listas Parte 2

#Crie um programa no qual o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
#matenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = []
pares = []
impares = []

for contador in range(1, 8):
    valores.append(int(input(f"Digite o {contador}º valor: ")))
    if(valores[0] % 2 == 0):
        pares.append(valores[0])
    else:
        impares.append(valores[0])
    valores.clear()
    pares.sort()
    impares.sort()

print("-=" * 25)

print(f"Os números pares digitados foram: {pares}")
print(f"Os números ímpares digitados foram: {impares}")