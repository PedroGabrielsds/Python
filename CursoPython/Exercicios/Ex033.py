#Exercicio aula 10

#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#V 1.0
#numero_1 = int(input("Digite o primeiro número: "))
#if(numero_1 > 0):
 #   numero_2 = int(input("Digite o segundo número: "))
  #  if(numero_2 > numero_1):
   #     maior = numero_2
    #    numero_3 = int(input("Digite o terceiro número:"))
     #   if(numero_3 > numero_2):
      #      maior = numero_3
       #     print(f"O maior número digitado é {maior}!")
        #else:
         #   print(f"O maior número digitado é {maior}!")
    #else:
     #   maior = numero_1
      #  numero_3 = int(input("Digite o terceiro número:"))
       # if(numero_3 > maior):
        #    maior = numero_3
         #   print(f"O maior número digitado é {maior}!")
        #else:
         #   print(f"O maior número digitado é {maior}!")
#else:
 #   print("O número digitado não é válido!!")

#V 2.0
#if(numero_1 == numero_2 == numero_3) or (numero_1 < 0 or numero_2 < 0 or numero_3 < 0):
 #   print("Erro: Os números digitados são iguais ou negativos!!")
#else:
 #   if(numero_1 > numero_2) and (numero_1 > numero_3):
   #     maior = numero_1
   #    menor = numero_2
    #    print(f"O maior número digitado é {maior}!")

    #elif(numero_2 > numero_3):
     #   maior = numero_2
      #  print(f"O maior número digitado é {maior}!")

    #else:
     #   maior = numero_3
      #  print(f"O maior número digitado é {maior}!")

numero_1 = int(input("Digite o primeiro número:"))
numero_2 = int(input("Digite o segundo número:"))
numero_3 = int(input("Digite o terceiro número:"))

menor = numero_1
if (numero_2 < numero_1) and (numero_2 < numero_3):
    menor = numero_2

if (numero_3 < numero_1) and (numero_3 < numero_2):
    menor = numero_3

maior = numero_1
if(numero_2 > numero_1) and (numero_2 > numero_3):
    maior = numero_2


if(numero_3 > numero_1) and (numero_3 > numero_2):
    maior = numero_3


print(f"O menor número digitado é {menor}!")
print(f"O maior número digitado é {maior}!")












