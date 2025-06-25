#Exercício Aula 16 - Tuplas

#Crie uma Tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time da Chapecoense.

times_brasilierao = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG', 'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio', 'Ceará SC', 'Vasco da Gama', 'São Paulo', 'Santos', 'EC Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport Recife')

print(f"Tabela Brasileirão 2025:", times_brasilierao)
print(f"=-" * 15)
print("Os 5 primeiros times são:",times_brasilierao[0:6])
print(f"=-" * 15)
print(f"Os 4 últimos times são:",times_brasilierao[16:20])
print(f"=-" * 15)
print(sorted(times_brasilierao))
print(f"=-" * 15)
print(f"O time da Chapecoense se encontra em 9º lugar da serie B")