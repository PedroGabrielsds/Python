#Ex049 - Aula 13

#Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

print("\033[1;33;40m-=\033[m" * 14)
print("\033[1;33;40m-=\033[m" * 5, "\033[1;32;40mTabuada\033[m", "\033[1;33;40m-=\033[m" * 4)
print("\033[1;33;40m-=\033[m" * 14)

tabuada_numero = int(input("Qual tabuada deseja ver? "))

for contador in range(1, 11):
    resultado = (tabuada_numero * contador)
    print(f"{tabuada_numero} X {contador} = {resultado}")
