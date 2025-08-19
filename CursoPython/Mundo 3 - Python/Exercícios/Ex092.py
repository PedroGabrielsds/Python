#Aula 19 - Dicionários

#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
#se por acaso o CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e
#acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = []
informaçoes = {}
ano_atual = date.today().year

informaçoes['nome'] = str(input(f"Nome: "))
informaçoes['nascimento'] = int(input(f"Ano de Nascimento: "))
informaçoes['idade'] = (ano_atual - informaçoes['nascimento'])
informaçoes['ctps'] = int(input(f"Carteira de Trabalho (0 não tem): "))
if(informaçoes['ctps'] == 0):
    print(f"-=" * 20)
    for key, value in informaçoes.items():
        if (key == 'ctps'):
            break
        else:
            print(f"{key} tem o valor {value}")

else:
    print(f"-=" * 20)
    informaçoes['contratacao'] = int(input(f"Ano de Contratação: "))
    informaçoes['salario'] = float(input(f"Salário: R$"))
    informaçoes['aposentadoria'] = ((35 - (ano_atual - informaçoes['contratacao'])) + informaçoes['idade'])
    for key, value in informaçoes.items():
        print(f"{key} tem o valor {value}")