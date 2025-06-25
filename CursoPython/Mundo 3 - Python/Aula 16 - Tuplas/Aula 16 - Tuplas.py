#Aula 16 - Tuplas

#Variáveis compostas - Tuplas

#Tuplas são imutáveis

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(f" a tupla lanche é composta por {lanche}")

for comida in lanche:
    print(f"Eu vou comer {comida}")

print(f"=-" * 10)

for contador in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[contador]} na posição {contador}")

print(f"-=" * 10)

for posicao, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {posicao}")

print(f"==-" * 10)

#Coloca em ordem alfabética
print(sorted(lanche))

print(f"Comi pra caramba!")

a = (2, 5, 4)
b = (5,8,1,2)
c = b + a
print(c)

#Mostra a posição que está um número na tupla
print(c.index(5, 1))

pessoa = ('Pedro', 20, 'M', 70)

#deleta a variável
del(pessoa)