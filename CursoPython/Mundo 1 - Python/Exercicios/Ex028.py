#Exercicio aula 10

#Escreva um progarma que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.

#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import  random

numero = random.randint(0,5)

print("Estou pensando em um número...")

sorte = int(input("Tente descobrir o número que pensei: "))

if(sorte == numero):
    print("Winner!! Na Mosca!! Você é o vencedor!")
    print("Pensamos no mesmo número!!")
else:
    print(f"LOSER! Pensei no número {numero} e você pensou no número {sorte}!!")
