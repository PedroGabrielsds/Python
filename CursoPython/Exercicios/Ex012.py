#Ex012 - Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto:

preco = float(input("Qual o preço do produto que deseja comprar? "))

print("Esse produto receberá 5% de desconto!")

desconto = float((preco * 5) / 100)

valor_final = float(preco - desconto)

print(f"Com o desconto seu produto sairá por: R${valor_final}!")