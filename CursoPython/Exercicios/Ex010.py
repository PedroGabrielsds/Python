#Ex010 - Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar:

dolar = float(3.27)

reais = float(input("Quantos reais você tem para comprar dólar: R$"))


dolares = float(reais / dolar)
print(f"Com R${reais:.2f} você consegue comprar {dolares:.2f} dólares!")