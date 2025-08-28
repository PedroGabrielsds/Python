#Aula 21 - Funções (Parte 2)

#Interactive Help:
#help(print)
# print(input.__doc__)
# help(input)

#=-=-=-=-=--===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Docstrings:
# def contador(inicio, fim, passo):
#     """
#     -> Realiza uma contagem e mostra na tela!
#     :param inicio: Inicio da contagem
#     :param fim: Fim da contagem
#     :param passo: passo da contagem
#     :return: Sem retorno
#     """
#     c = inicio
#     while c <= fim:
#         print(f"{c}", end=" ")
#         c += passo
#     print(f"Fim")
#
# #contador(2, 10, 2)
# help(contador)

#=-=-=-=-=--===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Argurmentos Opcionais:
# def somador(a, b, c = 0): #Se adicionar um valor a variável será considerado o valor padrão!
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela.
#     :param a: O primeiro valor
#     :param b: O segundo valor
#     :param c: O valor terceiro
#     :return: Sem retorno
#     Função Criada por Pedro Gabriel do STF
#     """
#     soma = a + b + c
#     print(f"{a} + {b} + {c} = {soma}")
#
# somador(1, 5)

#=-=-=-=-=--===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Escopo de vaiáveis:
# def funcao():
#     n1 = 4
#     print(f"N1 dentro vale {n1}")
#
#
# #Programa Principal
# n1 = 2
# funcao()
# print(f"N1 fora vale {n1}")

#=-=-=-=-=--===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Retorno de Resultados
def somador(a = 0, b = 0, c = 0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O valor terceiro
    :return: Sem retorno
    Função Criada por Pedro Gabriel do STF
    """
    soma = a + b + c
    return soma
    #print(f"{a} + {b} + {c} = {soma}")

soma_1 = somador(1, 2, 3)
soma_2 = somador(5, 3, 2)
soma_3 = somador(10, 2, 6)
print(soma_1)
print(soma_2)
print(soma_3)