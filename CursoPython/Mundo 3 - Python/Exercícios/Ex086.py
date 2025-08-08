#Aula 18 - Listas Parte 2

#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

#No final, mostre a matriz na tela, com a formatação correta.

fileira1 = []
fileira2 = []
fileira3 = []
tabela = [fileira1, fileira2, fileira3]

for c in range(0, 3):
    contador = 0
    while contador <= 2:
        tabela[c].append(int(input(f"Digite um número para a posição [{c}, {contador}]: ")))
        contador += 1

print("-=" * 25)

print(f"""[  {fileira1[0]}  ] [  {fileira1[1]}  ] [  {fileira1[2]}  ]
[  {fileira2[0]}  ] [  {fileira2[1]}  ] [  {fileira2[2]}  ]
[  {fileira3[0]}  ] [  {fileira3[1]}  ] [  {fileira3[2]}  ]""")