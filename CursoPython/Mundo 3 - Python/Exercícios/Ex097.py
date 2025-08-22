#Aula 20 - Funções (Parte 1):

#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como paramêtro e mostre uma mensagem com tamanho adaptável.

#Exemplo:
# escreva("Olá, Mundo!")

#Saída:
#-----------------
#   Olá, Mundo!
#-----------------

def escreva(txt):
    tamanho = len(txt) + 4
    print('-' * tamanho)
    print(f"{txt:^{tamanho}}")
    print('-' * tamanho)


#Programa Principal
frase = 1
while frase != 0:
    frase = str(input(f"Digite um título: "))
    escreva(frase)