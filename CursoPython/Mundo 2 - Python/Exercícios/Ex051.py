#Ex051 - Aula 13

#Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Proteção Aritimética). No final, mostre os 10
#primeiros termos dessa progressão

primeiro_termo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))

an = primeiro_termo + (10 - 1) * razao
sn = int((primeiro_termo + an) * 10 / 2)

qtd_termos = 0

for contador in range(primeiro_termo, sn + 1, razao):
    qtd_termos += 1
    if(qtd_termos < 11):
        print(f"{contador}", end=" --> ")

print(f"Acabou")