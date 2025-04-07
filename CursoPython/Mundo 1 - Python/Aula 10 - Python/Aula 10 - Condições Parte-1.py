#Aula 10 - Condições - Parte 1

#Exemplos:

tempo = int(input("Quantos anos tem seu carro? "))

if tempo <=3 :
    print("Seu carro é novo! :)")
else:
    print("Seu carro não é muito novo! :(")
print("--FIM--")

print('Carro novo' if tempo <=3 else 'Carro velho')
print("--FIM--")

nome = str(input("Qual é o seu nome? "))
if nome == "Pedro":
    print("Que lindo nome você tem! S3")
else:
    print("Seu nome é tão normal...")

print(f"Bom dia, {nome}!")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print(f"A sua média foi {media}")

if media >= 6.0:
    print("Sua média foi boa, parabéns!!")
else:
    print("Sua média não foi muito boa, estude mais!")

print('Parabéns!' if media >= 6.0 else 'Estude mais!')