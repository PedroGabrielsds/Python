#Aula 15 - Interrompendo repetições while

#Crie um programa que simule o funcionamento de um caixa eletrônico, No início, pergunte ao usuário qual será o valor a ser sacado
#(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

nota_cinquenta = 50
qtd_nota_cinquenta = 0
nota_vinte = 20
qtd_nota_vinte = 0
nota_dez = 10
qtd_nota_dez = 0
nota_um = 1
qtd_nota_um = 0
mackbank_icon = "MackBank"
mackbank_icon_colored = f"\033[1;31;49m{mackbank_icon}\033[m"

print(f"=" * 30)
print(f"{mackbank_icon_colored:^43}")
print(f"=" * 30)

valor = int(input(f"Qual valor deseja sacar? R$"))
if(valor >= 1):
    while(valor > 0):
        while(valor >= 50):
            valor -= nota_cinquenta
            qtd_nota_cinquenta += 1
        while(valor >= 20):
            valor -= nota_vinte
            qtd_nota_vinte += 1
        while(valor >= 10):
            valor -= nota_dez
            qtd_nota_dez += 1
        while(valor >= 1):
            valor -= nota_um
            qtd_nota_um += 1

print("-=" * 15)
if(qtd_nota_cinquenta != 0):
    print(f"Total de {qtd_nota_cinquenta} cédulas de R$50")
if(qtd_nota_vinte != 0):
    print(f"Total de {qtd_nota_vinte} cédulas de R$20")
if(qtd_nota_dez != 0 ):
    print(f"Total de {qtd_nota_dez} cédulas de R$10")
if(qtd_nota_um != 0):
    print(f"Total de {qtd_nota_um} cédulas de R$1")
print("=" * 30)