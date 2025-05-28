#Ex047 - Aula 13

#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

soma_pares = 0
soma_impares = 0

for contador in range(2, 51, 2):
    print(f"{contador},", end=" ")
    soma_pares += 1

    #pares = contador % 2
    #if(pares == 0):
     #   print(f"{contador},", end=" ")
      #  soma_pares += 1

    #else:
     #   soma_impares += 1

print(f"O total de números pares é: {soma_pares}!")