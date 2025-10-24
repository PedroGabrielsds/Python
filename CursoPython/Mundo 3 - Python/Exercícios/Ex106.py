#Aula 21 - Funções (Parte 2)

#Faça um mini-sistema que utilize o interactiveHelp do Python. O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar a palavra "Fim", o programa se encerrará.

#OBS: Usar cores.

from time import sleep

cores = ("\033[m",        #Desliga cor
         "\033[0;30;41m", #Cor 1 - Red
         "\033[0;30;42m", #Cor 2 - Green
         "\033[0;30;43m", #Cor 3 - Yellow
         "\033[0;30;44m", #Cor 4 - Blue
         "\033[0;30;45m", #Cor 5 - Purple
         "\033[0;30;47m", #Cor 6 - White
        );

def helplease(comando):
    """
    Função que usa o InteractiveHelp do Python
    :param comando: Recebe o comando que o usuário queira consultar o Help
    :return: Retorna o help de um comando específicado pelo usuário
    """
    sleep(1)
    print(cores[4], end="")
    mensagem(f"Acessando o manual do comando '{comando}'", 4)
    print(cores[0], end="")
    sleep(0.5)
    print(cores[6], end="")
    help(comando)
    print(cores[0], end="")

def mensagem(txt, cor=0):
    """
    Função que escreve um texto ou mensagem com cores e linhas
    :param txt: A mensagem ou texto que será escrito
    :param cor: Usa cores de fundo
    :return: Retorna o texto constumizado
    """
    tamanho = len(txt) + 4
    print(cores[cor], end="")
    print("~" * (tamanho))
    print(f"{f"{txt:^{tamanho}}"}")
    print("~" * (tamanho))
    print(cores[0], end="")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Programa Principal
comando = ""
while(comando != "fim"):
    mensagem('Sistema de Ajuda PyHelp', 2)
    comando = str(input(f"Função ou Biblioteca >> ")).lower().strip()
    if(comando != "fim"):
        helplease(comando)

mensagem("Até logo...", cor=1)