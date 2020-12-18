entrada = input().split(' ')
linhas = int(entrada[0])
colunas = int(entrada[1])
matriz = []
for i in range(linhas):
  linha = input().split()
  matriz.append(linha)

entrada2 = int(input())
bombas = []
for i in range(entrada2):
  ent = input().split(' ')
  posicao = [0, 0]
  a = int(ent[0])
  b = int(ent[1])
  posicao[0] = a
  posicao[1] = b
  bombas.append(posicao)

def procurarNavio(l, c):
  if matriz[l][c] == '.':
    return
  if matriz[l][c] == '#':
    matriz[l][c] = 0
    if matriz[l - 1][c] == '.':
      return
    if matriz[l - 1][c] == '#':
      procurarNavio(matriz[l - 1], matriz[l - 1][c])

for x in bombas:
  print(x)
  procurarNavio(x[0], x[1])

# procurarNavio(0, 0)

naviosDestruidos = 0
print(matriz)
