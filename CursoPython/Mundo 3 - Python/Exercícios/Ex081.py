#Aula 17 - Listas

#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:

#A) Quantos números foram digitados.

#B) A lista de valores, ordenada de forma decrescente.

#C) Se o valor 5 foi digitado e está ou não na lista.

resposta = 's'
contador = 1
qtd_cincos = 0
numeros = list()

while(resposta != "n"):
    numeros.append(int(input(f"Digite o {contador}º número: ")))
    contador += 1
    if(5 in numeros):
        qtd_cincos += 1
        print(5)
    resposta = str(input(f"Deseja digitar mais um número? [S/N] ")).lower().strip()[0]

numeros.sort(reverse=True)
print("=--=" * 15)
print(f"Ao todo \033[1m{contador}\033[m números foram digitados!")
print(f"A lista ordenada em ordem decrescente: {numeros}")
if(qtd_cincos == 1):
    print(f"O número 5 está presente na lista!")
elif(qtd_cincos > 1):
    print(f"O número 5 está presente e foram digitados \033[1m{qtd_cincos}\033[m vezes!")
else:
    print(f"O número 5 não está presente!")