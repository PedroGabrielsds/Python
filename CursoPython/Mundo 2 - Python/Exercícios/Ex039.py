#Ex039

#Exercicio Aula 12 - Condições Aninhadas

#Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:

#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar
#Se já passou da hora so tempo de alistamento

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

nome = str(input("Qual é o seu nome? "))
hora = datetime.datetime.now()
ano_atual = datetime.date.today().year

if(hora.strftime("%H:%M") <= "12:00"):
    cumprimento = "Bom dia"
elif(hora.strftime("%H:%M") >= "12:59") and (hora.strftime("%H:%M") <= "18:59"):
    cumprimento = "Boa tarde"
elif(hora.strftime("%H:%M") >= "19:59") and (hora.strftime("%H:%M") <= "23:59"):
    cumprimento = "Boa noite"

print(f"{cumprimento} {nome}, seja bem vindo ao \033[1:32:40malistamento militar!\033[m")

ano_nascimento = int(input("Qual seu ano de nascimento? "))
idade = (ano_atual - ano_nascimento)

print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}")

if(idade == 18):

    #print(f"\033[1;33;40mVocê possui {idade} anos de idade e já está na hora de se alistar!\033[m")
    print(f"\033[1;33;40mVocê tem que se alistar IMEDIATAMENTE!\033[m")

elif(idade > 18):

    atraso = idade - 18
    print(f"\033[1;31;40mVocê já deveria ter se alistado há {atraso} anos!\033[m")
    print(f"\033[1;33;40mSeu alistamento foi em {ano_atual - atraso}!\033[m")

    #resposta = str(input("Você já se alistou? [Sim/Não]"))
    #if(resposta == "Sim") or (resposta == "sim") or (resposta == "s") or (resposta == "ss") or (resposta == 'SS'):
     #   print(f"\033[1:33:40mVocê tem {idade} anos e já passou da fase do alistamento!\033[m")
    #else:
    #    print(f"\033[1:31:40mO tempo para se alistar já passou e você tem {atraso} ano(s) de atraso!\033[m")
    #    print(f"\033[1:31:40mIsso irá te gerar uma multa por não ter se alistado no momento correto!\033[m")

elif(idade <= 17):
    adianto = 18 - idade
    ano_alistamento = adianto + ano_atual
    #print(f"Assim que você completar 18 anos de idade, você precisa se alistar! \033[1;33;40mFaltam {adianto} anos para você se alistar!\033[m")
    print(f"\033[1;36;40mAinda faltam {adianto} anos para o alistamento!\033[m")
    print(f"\033[1;33;40mSeu alistamento será em {ano_alistamento}!\033[m")


