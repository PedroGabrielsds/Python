#Aula 15 - Interrompendo repetições while

#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
#No final mostre:

#A) Qual é o total gasto na compra;
#B) Quantos produtos custam mais de R$1000;
#C) Qual é o nome do produto mais barato.

produto = ""
preco = 0
maior_mil = 0
mais_barato = 0
compras = 0
total = 0
resposta = "S"

while(resposta != "N"):
    print(f"{"Mack-Ado":=^30}")
    compras += 1
    produto = str(input(f"Nome do produto: ")).strip()
    preco = float(input(f"Preço: R$"))
    total += preco
    if(compras == 1):
        mais_barato = preco
        nome_mais_barato = produto
    elif(preco < mais_barato):
        mais_barato = preco
        nome_mais_barato = produto

    if(preco > 1000):
        maior_mil += 1

    resposta = str(input(f"Deseja comprar mais produtos: [S/N] ")).upper().strip()[0]

print("=" * 30)
print(f"O total de suas compras é: R${total:.2f}")
print(f"{maior_mil} produtos custam mais de R$1.000!")
print(f"{nome_mais_barato} foi o produto mais barato desta compra, custando R${mais_barato:.2f}!")