#Aula 14 - Estrutura de repetição While

#Escreva um programa que leia um número n inteiro qualquer e mostre os n primeiros elementos de uma Sequência de Fibonacci

#Ex: 0 --> 1 --> 1 --> 2 --> 3 --> 5 --> 8

resposta = "S"

while(resposta != "N"):
    numero = int(input("Sequência de Fibonacci de "))
    t1 = 0
    print(f"{t1}", end=" --> ")
    t2 = 1
    print(f"{t2}", end=" --> ")
    for contador in range(3, numero + 1):
        t3 = t1 + t2
        print(t3, end=" --> ")
        t1 = t2
        t2 = t3
    print("Acabou!")
    resposta = str(input(f"Deseja ver outra sequência de Fibonacci? [S/N] ")).upper().strip()