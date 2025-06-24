#Aula 15 - Interrompendo repetições while

#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cado valor digitado pelo usuário. O programa
#será interrompido quando o número solicitado for negativo.

from time import sleep

print("-=" * 10)
print(f"{'Tabuada':-^20}")
print("-=" * 10)

numero = int(input(f"{'Tabuada de ':>15}"))

while(numero > 0):
    if(numero < 0):
        break
    else:
        contador = 1
        while(contador < 11):
            print(f"{f"{numero} X {contador} = {numero * contador}":^20}")
            contador += 1
        print(f"-=" * 10)
        numero = int(input(f"{'Outra tabuada: ':>17}"))

print(f"\033[1;31;40mEncerrando tabuada\033[m...")
sleep(1)