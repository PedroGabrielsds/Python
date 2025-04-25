#Ex043

#Exercicio Aula 12 - Condições Aninhadas

#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

#- Abaixo de 18,5: Abaixo do peso
#- Entre 18.5 e 25: Peso ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

print("\033[1;36;40mBem vindo(a) ao IMC Calculator\033[m")

altura = float(input("Qual é a sua altura? "))
peso = float(input("Qual é seu peso? (KG)"))
imc = peso / (altura ** 2)

print(f"Seu IMC atual é de {imc:.2f}")
if(imc < 18.5):
    print(f"Você está abaixo do peso ideal!")
elif(imc >= 18.5 and imc < 25):
    print(f"Você está no peso ideal!")
elif(imc >= 25 and imc < 30):
    print(f"Você está com sobrepeso!")
elif(imc >= 30 and imc < 40):
    print(f"Você está Obeso(a)!")
elif(imc >= 40):
    print(f"Você está com Obesidade Mórbida!")
