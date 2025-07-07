#Aula 17 - Listas

#valores = [8, 2, 5, 4, 9, 3, 0]
#print(valores)
#valores.sort()
#print(valores)
#valores.sort(reverse=True)
#print(valores)

#numeros = [2, 5, 9, 1]
#numeros[2] = 3
#numeros.append(7) #Adiciona o elemento especificado
#numeros.sort(reverse=True) #Escreve na ordem Crescente ou Descrescente
#numeros.insert(2, 0) #Adiciona o elemento em um lugar especifico
#numeros.pop(2) #Remove elementos especificado
#numeros.remove(2) #Remove elementos do valor especificado
#print(numeros)
#print(f"Essa lista tem {len(numeros)} elementos")

valor = list()
valor.append(int(input(f"Digite um valor: ")))
print(valor)

#Para ligar duas listas:
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(F"Lista A: {a}")
print(f"Lista B: {b}")

#Para copiar uma lista:
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")