#Ex041

#Exercicio Aula 12 - Condições Aninhadas

#A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria, de acordo com a idade:

#- Até 9 anos: Mirim
#- Até 14 anos: Infantil
#- Até 19 anos: Junior
#- Até 20 anos: Sênior
#- Acima: Master


print("\033[1;36;40m-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-\033[m")
print("\033[1;36;40m|\033[m  \033[1;32;40mSeja bem vindo à Confederação \033[m\033[1;33;40mNacional de Natação\033[m  \033[1;36;40m|\033[m")
print("\033[1;36;40m-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-\033[m")

idade = int(input("Digite sua idade e descubra sua categoria de nado: "))

if(idade <= 9):
    print(f"Idades abaixo de {idade} é da categoria: Mirim")
    print(f"Sua categoria de nado é: MIRIM")
elif(idade <= 14):
    print(f"Idades abaixo de {idade} são da categoria: Infantil")
    print(f"Sua categoria de nado é: Infantil")
elif(idade <= 19):
    print(f"Idades abaixo de {idade} são da categoria: Junior")
    print(f"Sua categoria de nado é: Junior")
elif(idade <= 20):
    print(f"Idades abaixo de {idade} são da categoria: Sênior")
    print(f"Sua categoria de nado é: Sênior")
else:
    print(f"Idades acima de {idade} são da categoria: Master")
    print(f"Sua categoria de nado é: Master")