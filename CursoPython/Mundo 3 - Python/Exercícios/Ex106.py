#Aula 21 - Funções (Parte 2)

#Faça um mini-sistema que utilize o interactiveHelp do Python. O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar a palavra "Fim", o programa se encerrará.

#OBS: Usar cores.

def escreva(frase):
    tamanho = len(frase)
    print("~" * tamanho)
    print(f"{frase:^{tamanho}}")
    print("~" * tamanho)

def helplease():
    resposta = "F"

    while(resposta != "FIM"):
        frase = escreva(f"\033[1;37;42mSISTEMA DE AJUDA PyHELP\033[m")
        comando = str(input(f"Função ou Biblioteca >> ")).lower().strip()
        if(comando != "FIM"):
            frase = escreva(f"\033[1;37;44mAcessando o manual do comando '{comando}'\033[m")
            manual = help(comando)
            print(manual)
            # print(f"\033[1;30;47m{manual}\033[m")
        else:
            frase = escreva((f"\033[1;37;41mSaindo\033[m"))
            break

#Programa Principal
helplease()