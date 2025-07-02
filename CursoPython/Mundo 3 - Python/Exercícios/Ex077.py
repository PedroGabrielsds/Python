#Exercício Aula 16 - Tuplas

#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada
#palavra, quais são as suas vogais.

tupla_palavras = ('Ponche', 'Amazon', 'Fiat', 'Chevrolet', 'Ford', 'Porsche', 'Mercedes', 'Cadeira', 'Carro', 'Pizza',
                  'Hamburguer', 'Salgado', 'Doce', 'Parede', 'Musica', 'Jogo')

for palavra in tupla_palavras:
    print(f"Em \033[1;39m{palavra}\033[m", end=" contém: ")
    palavra = palavra.lower()
    for letra in palavra:
        if(letra in "aeiou"):
            print(f"\033[1;39m{letra}\033[m, ", end="")
    print("")