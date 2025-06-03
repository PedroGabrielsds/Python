#Ex052 - Aula 13

#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

divisivel = 0

numero = int(input("Digite um número inteiro: "))

if(numero == 1):

    print(f"Número {numero} não é primo!")

else:
    for contador in range(1, numero + 1):
        if(numero % contador == 0):
            divisivel += 1
            print(f"\033[1;33;40m{contador}\033[m", end=" ")

        else:

            print(f"\033[1;31;40m{contador}\033[m", end=" ")

    print(f"")

    if(divisivel == 2):

        print(f"""O número {numero} foi divisível {divisivel} vezes!
E por isso ele é primo""")

    else:
        print(f"""O número {numero} não é primo, pois foi divisível {divisivel} vezes!!""")