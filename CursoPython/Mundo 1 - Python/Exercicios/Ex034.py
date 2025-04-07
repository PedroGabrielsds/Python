#Exercicio aula 10

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

#Para salários superiores a R$1.250,00, calcule um aumento de 10%.

#Para os inferiores ou iguais, o aumento é de 15%.

print("Calcule seu aumento salárial!")

salario = float(input("Digite seu salário atual: R$"))

if (salario <= 1250):

    aumento_salarial = (salario + (salario * 15 / 100))
    print(f"Seu salário vai receber um aumento de 15% e vai passar a ser R${aumento_salarial:.2f}")

elif (salario > 1250):

    aumento_salarial = (salario + (salario * 10 / 100))
    print(f"Seu salário vai receber um aumento de 10% e vai passar a ser R${aumento_salarial:.2f}")