#Aula 19 - Dicionários

# dicionarios = {}
# Ou
# dicionarios = dict()
#
# dados = dict()
# dados = {'nome':"Pedro", 'idade':21}
# dados['sexo'] = "M"
#
# print(dados['nome'])
# print(dados['idade'])
# print(dados['sexo'])
#
# del dados['sexo']
#
# print(dados)

# filme = {
#     'titulo':"Star Wars",
#     'ano':1977,
#     'diretor':"George Lucas"
# }
#
# print(filme.values()) #Pega somente os elementos.
# print(filme.keys()) #Pega somente os tipos.
# print(filme.items()) #Pega tanto tipo, tanto o elemento.
#
# for key, value in filme.items():
#     print(f"O {key} é {value}")

# estados = {}
# brasil = []

# for contador in range(0, 3):
#     estados['UF'] = str(input(f"Unidade Federativa: "))
#     estados['sigla'] = str(input(f"Sigla do Estado: "))
#     brasil.append(estados.copy())
#
# for estado in brasil:
#     for key, value in estado.items():
#         print(f"{key}, {value}")