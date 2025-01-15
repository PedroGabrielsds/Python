#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média:

aluno = (input("Qual o nome do aluno? "))

nota_1 = float(input(f"Primeira nota do aluno {aluno}: "))
nota_2 = float(input(f"Segunda nota do aluno {aluno}: "))
media = float((nota_1 + nota_2) / 2)

print(f"A média do aluno(a) {aluno} é: {media}")