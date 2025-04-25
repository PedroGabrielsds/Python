#Ex044
from time import sleep

#Exercicio Aula 12 - Condições Aninhadas

#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#- À vista dinheiro/cheque: 10% de desconto
#- À vista no cartão: 5% de desconto
#- Em até 2x no cartão: Preço normal
#- 3x ou mais no cartão: 20% de juros
import time
import pygame

pygame.init()
pygame.mixer.music.load('Ex044.mp3')
pygame.mixer.music.play()

print("\033[1;31;40m|=--=--=--=--=--=--=--=--=|\033[m \033[1;37;40mToy Store\033[m \033[1;31;40m|--=--=--=--=--=--=--=--=--=|\033[m")

valor_pagamento = float(input("\033[1;33;40mQual valor a ser pago?\033[m \033[1;32;40mR$\033[m"))

forma_pagamento = int(input("""\033[1;32;40m[1] - À vista dinheiro/Cheque com 10% de desconto)
[2] - À vista no cartão com 5% de desconto
[3] - Em até 2x no cartão
[4] - 3x ou mais no cartão\033[m
\033[1;33;40mInforme o método de pagamento:\033[m """))

if(forma_pagamento == 1):
    a_vista_dinheiro_cheque = (valor_pagamento - (valor_pagamento * 10) / 100)
    print(f"O valor final para o pagamento é de \033[1;32;40mR${a_vista_dinheiro_cheque:.2f}\033[m")

elif(forma_pagamento == 2):
    a_vista_cartao = (valor_pagamento - (valor_pagamento * 5 / 100))
    print(f"O valor final para o pagamento à vista no cartão é de \033[1;32;40mR${a_vista_cartao:.2f}")

elif(forma_pagamento == 3):
    dividido_duas_vezes = (valor_pagamento / 2)
    print(f"O valor final para o pagamento em 2x no cartão é de \033[1;32;40mR${dividido_duas_vezes:.2f}\033[m")

elif(forma_pagamento == 4):
    parcelas = int(input("\033[1;33;40mDividir em quantas vezes: \033[m"))

    if(parcelas < 3):
        dividido_duas_vezes = (valor_pagamento / 2)
        print(f"O valor final para o pagamento em 2x no cartão é de \033[1;32;40mR${dividido_duas_vezes:.2f}\033[m")
    elif(parcelas < 2):
        a_vista_cartao = (valor_pagamento - (valor_pagamento * 5 / 100))
        print(f"O valor final para o pagamento à vista no cartão é de \033[1;32;40mR${a_vista_cartao:.2f}")
    else:
        parcelado = (valor_pagamento / parcelas)
        parcela_com_juros = parcelado + (parcelado * 20 / 100)
        dividido_tres_ou_mais_vezes_com_juros = (valor_pagamento + (valor_pagamento * 20 / 100))
        print(f"Sua compra foi parcelada em {parcelas}x de R${parcela_com_juros:.2f} com juros!!")
        print(f"O valor final será \033[1;32;40mR${dividido_tres_ou_mais_vezes_com_juros:.2f}\033[m no final!!")
else:
    print(f"\033[1;31;40mO método de pagamento não existe!!\033[m")

time.sleep(30)








