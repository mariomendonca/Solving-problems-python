n = int(input())
fila = [None] * n
entradas = input().split()
for i in range(n):
  fila[i - 1] = int(entradas[i - 1])

d = int(input())
desistentes = [None] * d
entradas2 = input().split()
for i in range(d):
  desistentes[i - 1] = int(entradas2[i - 1])

for x in fila:
  for y in desistentes:
    if x == y:
      indice = fila.index(x)

      fila.pop(indice)

for i in fila:
  print(i, end=' ')


#lista encadeada classe