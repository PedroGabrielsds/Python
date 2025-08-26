#Aula 20 - Funções (Parte 1):

#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(valores):
    print(f"-=" * 25)
    print(f"Analisando os valores passados...")
    for valor in valores:
        print(f"{valor}", end=" ")

    print(f"Foram digitados {len(valores)} ao todo.")
    print(f"O maior valor digitado foi: {max(valores)}")


valores = (2, 9, 4, 5, 7, 1)
maior(valores)

valores = (4, 7, 0)
maior(valores)

valores = (1, 2)
maior(valores)

valores = (6, )
maior(valores)

valores = (0, )
maior(valores)