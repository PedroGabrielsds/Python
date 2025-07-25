#Aula 17 - Listas

#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

#teste com a expressao: (1 + (3 * 6) / 2)
parenteses = list()
numeros = list()
expressao = (input(f"Digite uma expressão: ")).replace(" ", "").strip().lower()

for elemento in expressao:
    if(elemento in "()"):
        parenteses.append(elemento)

if(len(parenteses) % 2 == 0):
    print(f"Sua expressão é válida!")
else:
    print(f"Sua expressão é inválida!")