#Aula 14 - Estrutura de repetição While
from tokenize import endpats

#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
#quando ele disser que quer mostrar 0 Termos.

resposta = 10
qtd_termos = 0
rodada = 0
resposta_str = "S"

while(resposta_str != "N"):
    print("=-" * 15)
    primeiro_termo = int(input(f"Primeiro Termo: "))
    razao = int(input(f"Razão: "))
    an = int((primeiro_termo + (resposta - 1) * razao))
    sn = int((primeiro_termo + an) * resposta / 2)

    while(resposta != 0):
        while(qtd_termos < resposta):
            qtd_termos += 1
            print(primeiro_termo, end=" --> ")
            primeiro_termo += razao
        print("Pausa!")
        qtd_termos_geral = resposta
        resposta_atual = resposta
        resposta = int(input(f"Quantos mais termos deseja ver: "))
        if(resposta > 0):
            resposta += resposta_atual
        elif(resposta == 0):
            resposta = 0

    print(f"Progressão finalizada com {qtd_termos_geral} termos mostrados!")
    resposta_str = str(input(f"Deseja ver uma nova Progressão Aritmética? [S/N] ")).upper().strip()
print("=-" * 15)
print(f"\033[1;31;40mEncerrado programa\033[m...")