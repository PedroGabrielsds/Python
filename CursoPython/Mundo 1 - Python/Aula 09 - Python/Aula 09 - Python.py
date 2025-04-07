#Aula 09 - Manipulando Texto

#Três Aspas em sequência seguirá as linhas de acordo com o texto!
#print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi.
#Vivamus sed nulla vitae eros interdum pharetra. Fusce tristique, purus sed eleifend egestas,
#felis purus aliquam metus, non auctor enim odio at ligula. Mauris volutpat sem in tortor placerat,
#ac aliquet orci iaculis. Suspendisse potenti. Proin malesuada, erat ac varius vehicula, urna ante pharetra magna,
#eget tempor felis felis non magna.""")

frase = "Curso em vídeo Python"

#=============-Fatiamento-================
#print(frase[3])
#print(frase[3:13])
#print(frase[:13])
#print(frase[13:])
#print(frase[1:15:2])
#print(frase[::2])
#==========================================

#=============-Análise-================
#print(len(frase))
#print(frase.count('o'))
#print(frase.count('o', 0, 13))
#print(frase.upper().count('O'))
#print(frase.find('Curso'))
#print(frase.lower().find('vídeo'))
#print('Curso' in frase)
#=======================================

#=============-Transformação-================
#print(frase.replace('Python', 'Android'))
#print(frase.upper())
#print(frase.lower())
#print(frase.capitalize()) - Deixa somente a primeira letra maiúscula
#print(frase.title()) - Deixe todas primeiras letras maiúsculas
#print(frase.strip()) - Remove os espaços antes e depois da string
#print(frase.rstrip()) - Direita
#print(frase.lstrip()) - Esquerda
#print(frase.split())
#dividido = frase.split()
#print(dividido)
#print(dividido [2] [3])
#Junção
#print('-'.join(dividido))
#==============================================






















dividido = frase.split()
print(dividido[0] [3])

