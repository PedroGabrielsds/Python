#Ex041

#Exercicio Aula 12 - Condições Aninhadas

#A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria, de acordo com a idade:

#- Até 9 anos: Mirim
#- Até 14 anos: Infantil
#- Até 19 anos: Junior
#- Até 20 anos: Sênior
#- Acima: Master

import datetime

print("\033[1;34;40m-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-\033[m")
print("\033[1;34;40m|\033[m  \033[1;32;40mSeja bem vindo a Confederação \033[m\033[1;33;40mNacional de Natação\033[m  \033[1;34;40m|\033[m")
print("\033[1;34;40m-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-\033[m")

ano_atual = datetime.date.today().year
ano_nascimento = int(input("Ano de nascimento: "))

idade = (ano_atual - ano_nascimento)

print(f"Quem nasceu em {ano_nascimento} tem {idade} anos de idade!")
if(idade <= 9):
    print(f"A categoria de nado para sua idade é: \033[1;35;40mMIRIM\033[m")
elif(idade <= 14):
    print(f"A categoria de nado para sua idade é: \033[1;34;40mInfantil\033[m")
elif(idade <= 19):
    print(f"A categoria de nado para sua idade é: \033[1;32;40mJunior\033[m")
elif(idade <= 20):
    print(f"A categoria de nado para sua idade é: \033[1;33;40mSênior\033[m")
else:
    print(f"A categoria de nado para sua idade é: \033[1;31;40mMaster\033[m")