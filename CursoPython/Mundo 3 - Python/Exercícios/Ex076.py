#Exercício Aula 16 - Tuplas

#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços. organizando os dados em forma tabular.

contador = 0
tupla_produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32,
                  "Canetas", 22.30, "Livro", 34.90)

print("=" * 30)
print(f"{'Produtos':<25}", end="Preço\n")
print("=" * 30)

for produto in range(0, len(tupla_produtos), 2):
    print(f"{tupla_produtos[produto]:.<24}", end=f"R${tupla_produtos[contador + 1]}\n")
    contador += 2