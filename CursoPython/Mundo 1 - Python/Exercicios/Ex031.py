#Exercicio aula 10

#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens até 200KM e R$0,45 para viagens mais longas.

distancia_viagem = float(input("Qual a distância da viagem? "))

if(distancia_viagem <= 200):
    valor_viagem = distancia_viagem * 0.50
    print(f"O valor da passagem para esta viagem é de: R${valor_viagem:.2f}")
else:
    valor_viagem = distancia_viagem * 0.45
    print(f"O valor da passagem para esta viagem é de: R${valor_viagem:.2f}")
