#Aula 21 - Funções (Parte 2)

#Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python.
#Só que fazendo a validação para aceitar apenas um valor numérico.

#Ex: n - leiaint("Digite um n: ")

def leiaint(pergunta):
    """
    Função Leiaint funciona como um input que só aceita números inteiros!
    :param pergunta: usa a mensagem passada pelo código principal para ser usada no input.
    :return n: Retorna o valor n se for do tipo inteiro.
    """
    controle = False
    while(controle == False):
        n = input(pergunta)
        if(n.isnumeric() == False):
            print(f"\033[1;31mError, Não foi digitado um número!!\033[m")
        else:
            controle = True
            return n

#Programa Principal
pergunta = leiaint("Digite um número: ")
print(f"Você digitou o número: {pergunta}")