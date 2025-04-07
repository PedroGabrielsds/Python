#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento:

salario = float(input("Qual é o valor do seu atual salário: R$"))

print(f"Parabéns você vai ganhar 15% de aumento no seu salário!")

aumento = ((salario * 15) / 100)

novo_salario = (aumento + salario)

print(f"O seu salário teve uma aumento de R${aumento} e ficou R${novo_salario:.2f}")