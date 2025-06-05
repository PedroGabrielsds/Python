#Aula 14 - Estrutura de repetição While

#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado,
#peça a digitação novamente até ter um valor correto

sexo = str(input(f"Informe o seu sexo: [M/F] ")).upper()

while((sexo != 'M') and (sexo != 'F')):
    sexo = str(input(f"\033[1;31;40mDado inválido\033[m, por favor informe seu sexo novamente: [M/F] ")).upper()

if(sexo == "M"):
    genero = "\033[1;34;40mMasculino\033[m"
else:
    genero = "\033[1;35;40mFeminino\033[m"

print(f"Sexo {genero} foi \033[1;33;40mregistrado com sucesso\033[m!!")




