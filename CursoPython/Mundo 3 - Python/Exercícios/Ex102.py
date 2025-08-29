#Aula 21 - Funções (Parte 2)

#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro
#chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(valor, show = False):
    """
    Esta função deve mostrar ou não o cálculo do fatorial de um valor passado pelo usuário!
    :param valor: Valor que será feito o fatorial
    :param show: Variável de controle para mostrar ou não o cálculo
    :return: Não foi usado nenhum retorno
    Função criada por Mack
    """
    factorial = 1
    if(show == True):
        print('--' * 20)
        for contador in range(valor, 0, - 1):
            if(contador >= 1):
                factorial *= contador

            if(contador >= 2):
                print(contador, end=" X ")
            elif(contador == 1):
                print(contador, end=f" = {factorial}\n")
    elif(show == False):
        factorial = 1
        for contador in range(valor, 0, -1):
            if(contador >= 1):
                factorial *= contador
        print('--' * 20)
        print(f"Fatorial de {valor} é igual: {factorial} \n")


#Programa Principal
valor = int(input(f"Fatorial de: "))
show = str(input(f"Deseja ver o calculo? [S/N] ")).upper().strip()[0]
if(show == "S"):
    fatorial(valor, show = True)
else:
    fatorial(valor, show = False)

help(fatorial)