#Ex054 - Aula 13

#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores de idade

from datetime import date

ano_atual = date.today().year
maiores_idade = 0
menores_idade = 0

for contador in range(1, 8):
    nome = str(input("Qual é o seu nome? "))
    ano_nascimento = int(input("\033[1;33;40mEm que ano você nasceu? \033[m"))
    idade = ano_atual - ano_nascimento
    if(idade >= 18):
        maiores_idade += 1
        #print(f"""\033[1;32;40mVocê já atingiu a maioridade!\033[m
#\033[1;33;40mVocê tem {idade} anos de idade {nome}!\033[m
#\033[1;31;40mBem vindo ao clube dos boletos!\033[m""")
    else:
        resto = 18 - idade
        menores_idade += 1
        #if(resto > 1):
            #plural = f"faltam {resto} anos"
            #print(f"\033[1;31;40mVocê ainda não atingiu a maioridade {nome}\033[m,\033[1;32;40m {plural} para completar 18 anos!\033[m")
        #else:
            #singular = f"falta {resto} ano"
            #print(f"\033[1;31;40mVocê ainda não atingiu a maioridade {nome}\033[m,\033[1;32;40m {singular} para completar 18 anos!\033[m")

print(f"{maiores_idade} pessoas são maiores de idade!")
print(f"{menores_idade} pessoas são menores de idade!")


