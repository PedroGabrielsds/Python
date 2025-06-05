#Aula 14 - Estrutura de repetição While

#Melhore o jogo do Desafio 028 onde o computador vai "Pensar" em um número 0 e 10. Só que agora o jogador vai tentar adivinhar
#até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

maquina = randint(0, 10)
contador = 1
cor = 31

print("\033[1;39;40m|==/==/==|\033[m\033[1;34;40mJogo Da Adivinhação\033[m\033[1;39;40m|==/==/==|\033[m")

print(f"===========|\033[1;{cor};40mPartida nº{contador}\033[m|===========")
print("Estou pensando em um número...")
palpite = int(input(f"Qual seu palpite? "))
print("Pensei no número:", maquina)
cor += 1

while(palpite != maquina):
    maquina = randint(0, 10)
    contador += 1
    print(f"===========|\033[1;{cor};40mPartida nº{contador}\033[m|===========")
    if(cor == 40):
        cor = 31
    else:
        cor += 1
    print("Estou pensando em um número...")
    palpite = int(input(f"Qual seu palpite? "))
    print("Pensei no número:", maquina)

if(contador == 1):
    print(f"Você acertou de primeira!! Parabéns!")

elif(contador >= 2):
    print(f"Você palpitou {contador} vezes para conseguir vencer!!")