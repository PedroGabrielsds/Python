#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m^2:

largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
area = float(largura * altura)

print(f"A área da sua parede é: {area}m²")

quantidade_tinta = float(area / 2)

print(f"Você precisa de {quantidade_tinta} litros de tinta para pintar sua parede!")