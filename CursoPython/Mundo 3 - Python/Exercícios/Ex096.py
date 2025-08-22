#Aula 20 - Funções (Parte 1):

#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento)
#e mostre a área do terreno.

def linha(txt):
    print('-' * 40)
    print(txt)
    print('-' * 40)


def area(largura, comprimento):
    resultado = largura * comprimento
    print(f"A área de um terreno {largura} X {comprimento} é de {resultado}m².")


#Programa Principal
linha(f"{'Controle de Terrenos': ^40}")
largura = float(input(f"Largura (m): "))
comprimento = float(input(f"Comprimento (m): "))
area(largura, comprimento)