#Exercicio aula 10

#Escreva um programa que leia a velocidade de um carro.

#Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.

#A multa vai custar R$7,00 por cada km acima do limite.

velocidade = float(input("Qual a velocidade do carro? "))

if(velocidade > 80):
    velocidade_acima = velocidade - 80
    multa = float(velocidade_acima * 7.00)
    print("Você foi mutado por excesso de velocidade! LIMITE: 80Km/h")
    print(f"O valor da multa será de: R${multa:.2f}!")
else:
    print("O carro passou com a velocidade dentro do limite!")