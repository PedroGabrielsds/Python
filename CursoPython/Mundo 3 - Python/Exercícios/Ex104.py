#Aula 21 - Funções (Parte 2)

#Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python.
#Só que fazendo a validação para aceitar apenas um valor numérico.

#Ex: n - leiaint("Digite um n: ")

n = input(f"Digite um valor: ")

if(n.isnumeric()):
    print(f"O valor é válido!!")
else:
    print(f"O valor não é válido!!")