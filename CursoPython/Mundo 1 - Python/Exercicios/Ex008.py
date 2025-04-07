#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros:

print("Conversor de metros para centimetros e milimetros!")

metros = float(input("Digite os metros que deseja converter: "))
cm = float(metros * 100)
mm= float(metros * 1000)

print(f"{metros} metros em centimetros é: {cm:.0f} centimetros")
print(f"{metros} metros em milimetros é: {mm:.0f} milimetros")