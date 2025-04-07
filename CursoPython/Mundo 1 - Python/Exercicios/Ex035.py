#Exercicio aula 10

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print("Descubra se é possível fazer um triângulo com seus valores e qual é o tipo deste triângulo!")

lado_a = int(input("Digite o valor do lado A: "))
lado_b = int(input("Digite o valor do lado B: "))
lado_c = int(input("Digite o valor do lado C: "))

if(lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
    print("É possível criar um triângulo com suas medidas!")
    if(lado_a == lado_b == lado_c):
        print(f"Seu triângulo é do tipo Equilátero, os três lados são iguais!")
    elif(lado_a == lado_b) or (lado_b == lado_c) or (lado_c == lado_a):
        print(f"Seu triângulo é do tipo Isósceles, existem dois lados iguais e um diferente!")
    else:
        print(f"Seu triângulo é do tipo Escaleno, todos os três lados são diferentes!")
else:
    print("Não é possível criar um triângulo com essas medidas!")