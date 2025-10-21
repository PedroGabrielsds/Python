#Aula 21 - Funções (Parte 2)

#Faça um mini-sistema que utilize o interactiveHelp do Python. O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar a palavra "Fim", o programa se encerrará.

#OBS: Usar cores.

def escreva(frase):
    tamanho = len(frase)
    print("\033[1;30;43m~\033[m" * tamanho)
    print(f"{frase:^{tamanho}}")
    print("\033[1;30;43m~\033[m" * tamanho)

def helplease():
    resposta = "F"

    while(resposta != "FIM"):
        frase = escreva(f"\033[1;30;43mSISTEMA DE AJUDA PyHELP\033[m")
        comando = str(input(f"Função ou Biblioteca > ")).lower().strip()
        if(comando != "FIM"):
            frase = escreva((f"Acessando o manual do comando '{comando}'"))
            frase = escreva(f"\033[1;m{help(comando)}")
        else:
            frase = escreva((f"\033[1;37;41mSaindo\033[m"))
            break


#Programa Principal
helplease()