#Aula 20 - Funções (Parte 1):

# def mostrarLinha(txt):
#     print('-' * 20)
#     print(txt)
#     print('-' * 20)
#
# mostrarLinha(f"{f'Tabela':^20}")
#
# mostrarLinha(f"Indice")

#-----------------------------------------------------------------

# def soma(a, b):
#     print(f"A = {a} e B = {b}")
#     s = a + b
#     print(f"A soma A + B = {s}")
#
# soma(a=4, b=5)
# soma(8, 9)
# soma(2, 1)

#-----------------------------------------------------------------

# def contador(* numero):
#     print(numero)
#
# contador(2, 1, 7)
# contador(8,0)
# contador(4, 4, 7, 6, 2)

#-----------------------------------------------------------------

# def dobra(lista):
#     posicao = 0
#     while posicao < len(lista):
#         lista[posicao] *= 2
#         posicao += 1
#
# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)