#Aula 18 - Listas Parte 2

#Aprimore o desafio anterior, mostrando no final:

#A) A soma de todos os valores pares digitados.

#B) A soma dos valores da terceira coluna.

#C) O maior valor da segunda linha.

fileira1 = []
fileira2 = []
fileira3 = []
tabelas = [fileira1, fileira2, fileira3]
soma_pares = 0

for c in range(0, 3):
    contador = 0
    while contador <= 2:
        tabelas[c].append(int(input(f"Digite um número para a posição: [{c}, {contador}]: ")))
        if(tabelas[c][contador] % 2 == 0):
            soma_pares += tabelas[c][contador]
        contador += 1

print("-=" * 25)

print(f"""[{fileira1[0]:^5}] [{fileira1[1]:^5}] [{fileira1[2]:^5}]
[{fileira2[0]:^5}] [{fileira2[1]:^5}] [{fileira2[2]:^5}]
[{fileira3[0]:^5}] [{fileira3[1]:^5}] [{fileira3[2]:^5}]
A soma dos valores \033[1mpares\033[m é: {soma_pares}
A soma dos valores da \033[1mterceira coluna\033[m é: {fileira1[2] + fileira2[2] + fileira3[2]}
O maior valor da segunda \033[1mLinha é\033[m {max(fileira2)}""")