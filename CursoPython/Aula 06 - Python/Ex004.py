#Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informações possiveis sobre ele

algo = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(algo))
print(f"É Alphanumerico: ",algo.isalnum())
print(f"São letras: ", algo.isalpha())
print(f"São números: ", algo.isnumeric())
print(f"É maiúsculo: ", algo.isupper())
print(f"É minúsculo: ", algo.islower())
print(f"É um titulo? ", algo.istitle())
print(f"Tem decimal? ", algo.isdecimal())
print(f"É espaço em branco? ", algo.isspace())