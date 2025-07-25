#Aula 17 - Listas

#Crie um programa no qual o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista. Já na posição
#correta de inserção (sem o usuário usar o sort()).

#No final, mostre a lista ordenada na tela.

numeros = list()

while(len(numeros) < 5):
    valor = int(input(f"Digite um número: "))
    if((len(numeros) == 0) or valor > numeros[len(numeros) - 1]):
        numeros.append(valor)
        print(f"Adicionado ao final da lista...")
    else:
        # valor = int(input(f"Digite um número: "))
        for posicao, numero in enumerate(numeros):
            if(valor <= numero):
                numeros.insert(posicao, valor)
                print(f"Adicionado na posição {posicao} da lista...")
                break
                # if (valor == numero):
                #     numeros.insert(posicao, valor)
                #     print(f"Adicionado na posição {posicao} da lista...")
                #     break
                # elif (valor < numero):
                #     numeros.insert(posicao, valor)
                #     print(f"Adicionado na posição {posicao} da lista...")
                #     break
                # elif (valor > numero):
                #     if (posicao + 1 == len(numeros) and valor > numero):
                #         numeros.append(valor)
                #         print(f"Adicionado ao final da lista...")
                #         break

print(f"-=-=" * 20)
print(f"Os valores digitados em ordem foram {numeros}")