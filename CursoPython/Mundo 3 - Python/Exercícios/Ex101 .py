#Aula 21 - Funções (Parte 2)

#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.

from datetime import date

def voto(ano_nascimento):
        """
        Esta função é usada para saber se o voto do usuário é ou não necessário de acordo com a idade o usuário!

        :param ano_nascimento: Recebe o ano de nascimento para calcular a idade do usuário.
        :return: Sem retorno
        Função Criada Por Mack
        """
        idade = (date.today().year - ano_nascimento)
        if(idade < 18):
            print(f"Com {idade} anos: \033[1;31mNão vota\033[m!")
        elif(idade > 18 and idade < 70):
            print(f"Com {idade} anos: Voto \033[1;33mOBRIGATÓRIO\033[m!")
        elif(idade >= 70):
            print(f"Com {idade} anos: Voto \033[1;32mOPCIONAL\033[m!")

ano_nascimento = int(input(f"Em que ano você nasceu? "))
voto(ano_nascimento)