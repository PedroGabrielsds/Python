#Aula 14 - Estrutura de repetição While

#Crie um programa que leia dois valores e mostre um menu na tela:
#[1]Somar
#[2]Multiplicar
#[3]Maior
#[4]Novos Números
#[5]Sair do Programa

#Seu programa deverá realizar a operação solicitada em cada caso

opcao = 0

while(opcao != 5):
    print(f"================| Inicio |==================")
    valor_1 = int(input(f"Digite um valor: "))
    valor_2 = int(input(f"Digite mais um valor: "))
    print(f"================|  Menu  |====================")
    opcao = int(input("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
Sua opção: """))

    if(opcao == 1):
        soma = valor_1 + valor_2
        print(f"A soma entre {valor_1} e {valor_2} resulta em {soma}")

    elif(opcao == 2):
        multiplicacao = valor_1 * valor_2
        print(f"""Multiplicação:
{valor_1} X {valor_2} = {multiplicacao}""")

    elif(opcao == 3):
        if((valor_1 > valor_2) or (valor_1 == valor_2)):
            print(f"O maior valor digitado foi {valor_1}")
        else:
            print(f"O maior valor digitado foi {valor_2}")

print(f"\033[1;31;40mSaindo do programa\033[m...")