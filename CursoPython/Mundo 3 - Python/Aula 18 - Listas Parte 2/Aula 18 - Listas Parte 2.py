#Aula 18 - Listas Parte 2

# pessoas = [["Pedro", 21], ["Maria", 22], ["João", 35]]

# print(pessoas[0][1])
# print(pessoas[1][1])
# print(pessoas[2][0])
# print(pessoas[1])

# teste = []
# teste.append("Pedro")
# teste.append(21)
# galera = []
# galera.append(teste[:])
# #Realiza uma ligação entre as listas
# teste[0] = "Maria"
# teste[1] = 22
# galera.append(teste[:])
# #Realiza uma cópia
# print(galera)

galera = list()
dados = list()
qtd_maior = 0
qtd_menor = 0

for contador in range(1, 5):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()

for pessoa in galera:
    if(pessoa[1] >= 18):
        print(f"{pessoa[0]} é maior de idade e tem {pessoa[1]} anos!")
        qtd_maior += 1
    else:
        print(f"{pessoa[0]} é menor de idade e tem {pessoa[1]} anos!")
        qtd_menor += 1

print(f"No total temos {qtd_maior} pessoa(s) de maior")
print(f"E {qtd_menor} pessoa(s) menor de idade!")