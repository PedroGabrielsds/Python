#Exercício Aula 16 - Tuplas

#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

valor_1 = int(input(f"Digite o primeiro número: "))
valor_2 = int(input(f"Digite o segundo número: "))
valor_3 = int(input(f"Digite o terceiro número: "))
valor_4 = int(input(f"Digite o quarto número: "))
par_1 = par_2 = par_3 = par_4 = 0
qtd_noves = 0
vezes_tres = 0
posicao_primeiro_tres = 0

tupla = (valor_1, valor_2, valor_3, valor_4)

for posicao, valor in enumerate(tupla):
    if(valor == 9):
        qtd_noves += 1

    if(valor == 3):
        if(vezes_tres == 1):
            break
        else:
            posicao_primeiro_tres = posicao
            vezes_tres += 1

    if(posicao == 0):
        par_0 = valor
    elif(posicao == 1):
        par_1 = valor
    elif(posicao == 2):
        par_2 = valor
    elif(posicao == 3):
        par_3 = valor

print(f"O valor 9 apareceu {qtd_noves} vezes!")
if(posicao_primeiro_tres == 0):
    print(f"Não foi digitado nenhum número três!")
else:
    print(f"O primeiro valor 3 apareceu na posição: {posicao_primeiro_tres + 1}º ")

print(f"Os números pares apresentados foram: ", end="")
if(par_1 == 0 and par_2 == 0 and par_3 == 0 and par_4 == 0):
    print(f"Não foram apresentados nenhum número par!")
else:
    for posicao, numero in enumerate(tupla):
        if(numero > 0 and numero % 2 == 0):
            if(posicao == 3):
                print(f"{numero}")
            else:
                if(posicao == 2 and tupla[3] % 2 == 0):
                    print(f"{numero}", end=", ")
                else:
                    print(f"{numero}", end=" ")