#Aula 15 - Interrompendo repetições while

#O break é uma instrução de controle de fluxo usada para interromper imediatamente a execução de um loop (for ou while),
#mesmo que a condição do loop ainda seja verdadeira.

numero = 0
soma = 0

while True:
    numero = int(input(f"Digite um número: "))
    if(numero == 999):
        break
    else:
        soma += numero

print(f"A soma é {soma}")