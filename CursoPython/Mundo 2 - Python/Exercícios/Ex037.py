#Ex037

#Exercicio Aula 12 - Condições Aninhadas

#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

#-1 para binário
#-2 para octal
#-3 para hexadecimal

numero = int(input("Digite um número inteiro para realizar a conversão: "))

print("""[1] para converter para BINÁRIO
[2] para converter para OCTAL
[3] para converter para HEXADECIMAL""")
escolha = int(input("Sua escolha: "))

if(escolha == 1):
    resultado = bin(numero)[2:]
    print(f"O número {numero} em BINÁRIO é: \033[1;33;40m{resultado}\033[m")

elif(escolha == 2):
    resultado = oct(numero)[2:]
    print(f"O número {numero} em OCTAL é: \033[1;33;40m{resultado}\033[m")

else:
    resultado = hex(numero)[2:]
    print(f"O número {numero} em HEXADECIMAL é: \033[1;33;40m{resultado}\033[m")
