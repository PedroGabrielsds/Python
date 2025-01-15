#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada:

print("Descubra o dobro, triplo e a raiz quadrada!")
numero = int(input("Digite um número: "))

dobro = (numero * 2)
triplo = (numero * 3)
raiz_quadrada = (numero**(1/2))

print(f"O dobro de {numero} é {dobro}")
print(f"O triplo de {numero} é {triplo}")
print(f"A raiz quadrada de {numero} é {raiz_quadrada}")