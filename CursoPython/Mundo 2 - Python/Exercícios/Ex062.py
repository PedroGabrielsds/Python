#Aula 14 - Estrutura de repetição While

#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
#quando ele disser que quer mostrar 0 Termos.

resposta = "s"

while(resposta != "n"):
    primeiro_termo = int(input(f"Digite o primeiro Termo: "))
    razao = int(input(f"Digite a razão: "))
    an = int(primeiro_termo + (10 - 1) * razao)
    sn = int((primeiro_termo + an) * 10 / 2)

    qtd_termos = 0

    for contador in range(primeiro_termo, sn + 1, razao):
        qtd_termos += 1
        if(qtd_termos < 11):
            print(f"{contador}", end=" --> ")
    print(f"Acabou!")
    resposta = str(input("Deseja realizar outra Progressão Aritmética? "))