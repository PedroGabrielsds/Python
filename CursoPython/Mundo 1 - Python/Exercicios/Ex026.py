#Faça um programa que leia uma frase pelo teclado e mostre:
#Exercicio Aula 09

#-> Quantas vezes aparece a letra "A";
#-> Em que posição ela aparece a primeira vez;
#-> Em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).strip().lower()

print(f"Na frase digitada contém {frase.count('a')} letra(s) 'A'")

print(f"A letra 'A' aparece a primeira vez na posicão: {frase.find('a')}")

print(f"A letra 'A' aparece a última vez na posicão: {frase.rfind('a')}")


