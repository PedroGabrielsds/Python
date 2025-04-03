#Exercicio aula 10

#Faça um programa que leia um ano qualquer e mostre se ele é Bissexto!

import datetime #módulo que importa a data do computador!

ano = int(input("Digite um ano e verifique se é bissexto ou não: "))

#if((ano % 4 == 0) and (ano % 100 > 0)) or ((ano % 4 == 0) and (ano % 100 == 0) and (ano % 400 == 0)):
 #   print(f"O ano {ano} é bissexto e contém 366 dias!")
#else:
  #  print(f"O ano {ano} não é bissexto!")

if(ano == 0):
    ano = datetime.date.today().year

if (ano % 4 == 0) and (ano % 100 != 0):
    print(f"O ano {ano} é bissexto!")
elif (ano % 100 == 0) and (ano % 400 == 0):
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")

