#Exercício Aula 16 - Tuplas

#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

contagem_extensa = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenovo', 'vinte')

print(f"Contando por Extenso")
print(f"=-" * 15)
resposta = 's'

while(resposta != "n"):
    numero = int(input(f"Digite um número entre 0 e 20: "))
    print(contagem_extensa[numero])

    resposta = str(input(f"Deseja ver outro número: [S/N] ")).lower().strip()[0]
    while(resposta != 's' and resposta != 'n'):
        print(f"Opção \033[1;31minválida\033[m, tente novamente!")
        resposta = str(input(f"Deseja ver outro número: [S/N] ")).lower().strip()[0]