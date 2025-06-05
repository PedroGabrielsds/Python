#Aula 14 - Estrutura de repetição While

#================================
contador = 1

while(contador < 11):
    print(f"{contador}..", end=" ")
    contador += 1

print(f"Terminei de contar!")

#================================

#================================
numero = 1

while(numero != 0):
    numero = int(input(f"Digite um número: "))

print(f"Sessão encerrada!")

#================================

resposta = "s"

while(resposta != "n"):
    numero = int(input(f"Digite um número: "))
    resposta = str(input(f"Deseja continuar? [s/n] \n")).lower()

print(f"Fim...")

#================================

numero = 1
pares = impar = 0

while(numero != 0):
    numero = int(input(f"Digite um número: "))
    if(numero % 2 == 0):
        pares += 1
    else:
        impar += 1

print(f"Você digitou {pares} números pares e {impar} números ímpares!!")