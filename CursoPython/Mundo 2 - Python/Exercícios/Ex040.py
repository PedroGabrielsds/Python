#Ex040

#Exercicio Aula 12 - Condições Aninhadas

#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
#com a média atingida:

#- Média abaixo de 5.0:
#Reprovado

#- Média entre 5.0 e 6.9:
#Recuperação

#- Média 7.0 ou superior:
#Aprovado
print(f"\033[1;37;40m=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=\033[m")

aluno = str(input("Qual o nome do aluno(a): "))
nota_1 = float(input(f"Digite a primeira nota de {aluno}: "))
nota_2 = float(input(f"Digite a segunda nota de {aluno}: "))

media_nota = (nota_1 + nota_2) / 2

if (media_nota < 5.0):
    print(f"A média do aluno(a) \033[1;36;40m{aluno}\033[m foi: \033[1;31;40m{media_nota:.2f}\033[m!")
    print(f"Portanto, o aluno \033[1;36;40m{aluno}\033[m foi \033[1;31;40mREPROVADO\033[m!")
elif(media_nota > 5.0) and (media_nota < 6.9):
    print(f"A média do aluno(a) \033[1;36;40m{aluno}\033[m foi: \033[1;33;40m{media_nota:.2f}\033[m!")
    print(f"Portanto, o aluno(a) \033[1;36;40m{aluno}\033[m está de \033[1;33;40mRECUPERAÇÃO\033[m!")
elif(media_nota >= 7.0):
    print(f"A média do aluno(a) \033[1;36;40m{aluno}\033[m é \033[1;32;40m{media_nota:.2f}\033[m")
    print(f"Portanto o aluno(a) \033[1;36;40m{aluno}\033[m está \033[1;32;40mAprovado(a)\033[m!")

print(f"\033[1;37;40m=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=\033[m")