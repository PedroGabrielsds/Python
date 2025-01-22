#Faça um programa que leia o comprimento de cateto oposto
#e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
cateto_oposto = float(input("Qual o comprimento do cateto oposto? "))

cateto_adjacente = float(input("Qual o comprimento do cateto adjacente? "))

hipotenusa = float(math.hypot(cateto_oposto, cateto_adjacente))

print(f"O valor da hipotenusa é {hipotenusa:.2f}")

