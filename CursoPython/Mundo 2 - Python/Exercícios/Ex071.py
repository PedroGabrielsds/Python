#Aula 15 - Interrompendo repetições while

#Crie um programa que simule o funcionamento de um caixa eletrônico, No início, pergunte ao usuário qual será o valor a ser sacado
#(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = 0

print(f"=" * 17)
print(f"{'\033[1;31;40mMackBank\033[m':=^30}")

opcao = int(input(f"""[1] Sacar
[2] Depositar
[3] Extrato
[4] Sair
Escolha uma opção: """))

if(opcao == 1):
    while(valor < 0):
        nota_cinquenta = 0
        nota_vinte = 0
        nota_dez = 0
        nota_um = 0
        valor = int(input(f"Qual valor a ser sacado? R$"))
        #sacar = int(input(f"""          Sacar em cédulas de:
          #[1] R$50
          #[2] R$20
          #[3] R$10
          #[4] R$1
          #Escolha uma opção: """))
        if(valor >= 1):
            while(valor >= 50):
                valor -= 50
                nota_cinquenta += 1
                #if(valor <= 50):

            while(valor >= 20):
                valor -= 20
                nota_vinte += 1
                #if(valor < 20):

            while(valor >= 10):
                valor -= 10
                nota_dez += 1
                #if(valor < 10):

            while(valor >= 1):
                valor -= 1
                nota_um += 1
                #if(valor < 1):
        else:
            valor = float(input(f"Esse valor não pode ser sacado! Tente outro valor de saque: "))
else:
    print(f"Opção \033[1;31mindisponível\033[m no momento, por favor tente outra opção!")



