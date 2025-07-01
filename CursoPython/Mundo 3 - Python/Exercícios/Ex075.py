#Exercício Aula 16 - Tuplas

#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

par_1 = par_2 = par_3 = par_4 = 0
qtd_noves = 0
vezes_tres = 0
posicao_primeiro_tres = 0

tupla = (int(input(f"Digite o 1º número: ")), int(input(f"Digite o 2º número: ")), int(input(f"Digite o 3º número: ")), int(input(f"Digite o 4º número: ")))

for posicao, valor in enumerate(tupla):
    if(posicao == 0):
        par_0 = valor
    elif(posicao == 1):
        par_1 = valor
    elif(posicao == 2):
        par_2 = valor
    elif(posicao == 3):
        par_3 = valor

print(f"O valor 9 apareceu {tupla.count(9)} vezes!")
if(3 not in tupla):
    print(f"Não foi digitado nenhum número três!")
else:
    print(f"O primeiro valor 3 apareceu na {tupla.index(3, 0) + 1}ª posição!")

print(f"Os números pares apresentados foram: ", end="")
if(par_1 == 0 and par_2 == 0 and par_3 == 0 and par_4 == 0):
    print(f"Não foram apresentados nenhum número par!")
else:
    for posicao, numero in enumerate(tupla):
        if(numero > 0 and numero % 2 == 0):
            if(posicao == 2 and tupla[3] % 2 != 0):
                print(f"{numero}", end="")
            elif(posicao == 3):
                print(f"{numero}", end="")
            else:
                print(f"{numero}", end=", ")