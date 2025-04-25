#Ex042

#Exercicio Aula 12 - Condições Aninhadas

#Refaça o EX035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#- Equilátero: Todos os lados iguais

#- Isósceles: Dois lados iguais

#- Escaleno: Todos os lados diferentes

print(f"\033[1;34;40mVerifique o tipo de triângulo que será criado com suas medidas!\033[m")

lado_1 = int(input("Digite a medida do primeiro lado: "))
lado_2 = int(input("Digite a medida do segundo lado: "))
lado_3 = int(input("Digite a medida do terceiro lado: "))

equilatero = "Seu triângulo é \033[1;35;40mEquilátero\033[m!"
isosceles = "Seu triângulo é \033[1;34;40mIsósceles\033[m!"
escaleno = "Seu triângulo é \033[1;33;40mEscaleno!"

if((lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1)):
    if(lado_1 == lado_2) and (lado_2 == lado_3):
        print(equilatero)
    elif(lado_1 == lado_2) or (lado_1 == lado_3) or (lado_2 == lado_3):
        print(isosceles)
    elif(lado_1 != lado_2) and (lado_2 != lado_3):
        print(escaleno)
else:
    print("Não é possível criar um triângulo com essas medidas!")