#Aula 12 - Condições Aninhadas

nome = str(input("Qual é seu nome? "))

if(nome == 'Pedro'):
    print("Seu nome é extremamente bonito!")
elif(nome == 'João' or nome == 'Maria' or nome == 'Paulo'):
    print("Seu nome é bem popular no Brasil!")
elif(nome in 'Ana Cláudia Andressa Juliana Melissa'):
    print("Belo nome feminino!")
else:
    print("Seu nome é bem normal!")

print(f"Tenha uma boa tarde {nome}!")