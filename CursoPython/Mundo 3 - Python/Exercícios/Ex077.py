#Exercício Aula 16 - Tuplas

#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada
#palavra, quais são as suas vogais.

tupla_palavras = ('Ponche', 'Amazon', 'Fiat', 'Chevrolet', 'Ford', 'Porsche', 'Mercedes', 'Cadeira', 'Carro', 'Pizza',
                  'Hamburguer', 'Salgado', 'Doce', 'Parede', 'Musica', 'Jogo')


for palavra in tupla_palavras:
    palavra_dividida = palavra.lower().split()
    print(palavra_dividida[0] [palavra_dividida.count('a')])
    #print(f"A palavra: {palavra} contém {contagem_vogais}, sendo elas: {}")