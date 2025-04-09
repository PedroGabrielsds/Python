#Ex036

#Exercicio Aula 12 - Condições Aninhadas

#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print("\033[1;37;40m|--=--=--=--=--=--=--=--=--=--=--=--=--=--|\033[m")
print("\033[1;37;40m|--=--=--=-\033[m \033[1;31;40mBem vindo ao MackBank\033[m \033[1;37;40m-=--=--=|\033[m")
print("\033[1;37;40m|--=--=--=--=--=--=--=--=--=--=--=--=--=--|\033[m")

#Coleta de dados para o possível empréstimo
print("\033[1;33;40mPeça seu empréstimo aqui\033[m")
valor_casa = float(input("Qual é o valor da casa?"))
valor_salario = float(input("Qual seu salário atual? "))
pay_years = int(input("Em quantos anos pretende pagar o empréstimo? "))

valor_parcela = valor_casa / (pay_years * 12)

porcentagem_salario = valor_salario * 30 / 100

if(valor_parcela > porcentagem_salario):
    print(f"\033[1;31;40mPara pagar uma casa de R${valor_casa} em {pay_years} anos a prestação será de R${valor_parcela:.2f}\033[m")
    print("Seu empréstimo foi \033[1;31;40mNEGADO!!\033[m")

else:
    print("\033[1;32;40mParabéns, você conseguiu o seu empréstimo e conseguirá comprar sua casa!!\033[m")
    print(f"Sua parcela ficou no valor de \033[1;32;40mR${valor_parcela:.2f}\033[m por mês durante \033[1;33;40m{pay_years}\033[m anos!")